import json
import boto3
from datetime import datetime
from urllib.parse import unquote_plus

# AWS Clients
rekognition = boto3.client("rekognition")
dynamodb = boto3.resource("dynamodb")
sns = boto3.client("sns")
sqs = boto3.client("sqs")

# ==========================
# CHANGE THESE VALUES
# ==========================
TABLE_NAME = "airport-security-system"

TOPIC_ARN = "arn:aws:sns:ap-south-1:163114508321:airport-security"

QUEUE_URL = "https://sqs.ap-south-1.amazonaws.com/163114508321/airport-security-pranav"
# ==========================

table = dynamodb.Table(TABLE_NAME)

WEAPON_LABELS = [
    "Knife",
    "Gun",
    "Weapon",
    "Firearm",
    "Pistol",
    "Rifle",
    "Bomb",
    "Explosive",
    "Ammunition"
]


def lambda_handler(event, context):

    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    image_name = unquote_plus(
        event["Records"][0]["s3"]["object"]["key"]
    )

    print(f"Image Uploaded : {image_name}")

    response = rekognition.detect_labels(
        Image={
            "S3Object": {
                "Bucket": bucket,
                "Name": image_name
            }
        },
        MaxLabels=20,
        MinConfidence=70
    )

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for label in response["Labels"]:

        label_name = label["Name"]
        confidence = round(label["Confidence"], 2)

        print(f"{label_name} : {confidence}%")

        # Send to SQS
        sqs.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=json.dumps({
                "ImageName": image_name,
                "Label": label_name,
                "Confidence": confidence,
                "Timestamp": timestamp
            })
        )

        print("Message Sent to SQS")

    # Read messages from SQS
    messages = sqs.receive_message(
        QueueUrl=QUEUE_URL,
        MaxNumberOfMessages=10,
        WaitTimeSeconds=2
    )

    if "Messages" not in messages:
        print("No messages in queue")
        return {
            "statusCode": 200,
            "body": "No messages found"
        }

    for msg in messages["Messages"]:

        body = json.loads(msg["Body"])

        image = body["ImageName"]
        label = body["Label"]
        confidence = body["Confidence"]
        timestamp = body["Timestamp"]

        # Store in DynamoDB
        table.put_item(
            Item={
                "ImageName": image,
                "Label": label,
                "Confidence": str(confidence),
                "Timestamp": timestamp
            }
        )

        print("Stored in DynamoDB")

        # SNS Alert
        if label in WEAPON_LABELS:

            sns.publish(
                TopicArn=TOPIC_ARN,
                Subject="Airport Security Alert",
                Message=f"""
🚨 AIRPORT SECURITY ALERT 🚨

Weapon Detected

Image Name : {image}

Weapon : {label}

Confidence : {confidence} %

Time : {timestamp}
"""
            )

            print("SNS Alert Sent")

        # Delete processed message
        sqs.delete_message(
            QueueUrl=QUEUE_URL,
            ReceiptHandle=msg["ReceiptHandle"]
        )

    return {
        "statusCode": 200,
        "body": json.dumps("Processing Completed")
    }