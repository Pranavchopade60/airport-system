# ✈️ Airport Security System using Amazon Rekognition

A cloud-based **Airport Security System** built using **Amazon Rekognition, AWS Lambda, Amazon API Gateway, Amazon S3, Amazon DynamoDB, Amazon SNS, EC2, HTML, CSS, and JavaScript**. The application enables airport security personnel to upload baggage or surveillance images, automatically detect prohibited or suspicious objects using Amazon Rekognition, securely store inspection results, and send real-time alerts for enhanced airport security.

---

```

---

# 📸 Screenshots

## Dashboard

![Dashboard](airpot-security.png)

---


# ✨ Features

- Upload Baggage or Surveillance Images
- Automatic Object Detection using Amazon Rekognition
- Detect Suspicious or Restricted Objects
- Store Detection Results in DynamoDB
- Upload Images to Amazon S3
- Real-Time Security Alerts using Amazon SNS
- REST API using Amazon API Gateway
- Cloud Hosted Dashboard
- Responsive Interface
- Serverless Backend
- CloudWatch Monitoring
- Fast Image Processing

---

# 🏗 Architecture

```
Security Officer
        │
        ▼
Amazon EC2 (Web Dashboard)
        │
        ▼
Amazon API Gateway
        │
        ▼
AWS Lambda
        │
        ├──────────────► Amazon S3
        │                     │
        │                     ▼
        │            Stored Security Images
        │
        ├──────────────► Amazon Rekognition
        │                     │
        ▼                     ▼
Amazon DynamoDB        Detected Objects
        │
        ▼
Amazon SNS
        │
        ▼
Security Alert Notification
```

---

# ☁️ AWS Services Used

- Amazon EC2
- Amazon S3
- Amazon Rekognition
- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- Amazon SNS
- AWS IAM
- Amazon CloudWatch

---

# 💻 Tech Stack

## Frontend

- HTML5
- CSS3
- JavaScript (Vanilla)

## Backend

- Python
- AWS Lambda

## Cloud Services

- Amazon Rekognition
- Amazon S3
- Amazon DynamoDB
- Amazon SNS
- Amazon API Gateway
- Amazon EC2
- AWS IAM
- Amazon CloudWatch

---

# 📁 Project Structure

```
Airport-Security-System
│
├── frontend
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   └── assets
│
├── lambda
│   ├── uploadImage.py
│   ├── detectObjects.py
│   ├── getHistory.py
│   └── sendAlert.py
│
├── screenshots
│   ├── dashboard.png
│   ├── upload-image.png
│   ├── detection-result.png
│   └── history.png
│
└── README.md
```

---

# ⚙️ API Endpoints

## Upload Image

```
POST /upload
```

Request Body

```json
{
    "image": "base64EncodedImage"
}
```

---

## Get Detection Result

```
GET /result?id=123
```

---

## Inspection History

```
GET /history
```

---

## Send Alert

```
POST /alert
```

---

# 🔍 Detection Workflow

1. Security officer uploads an image.
2. Image is stored in Amazon S3.
3. AWS Lambda invokes Amazon Rekognition.
4. Rekognition detects labels and confidence scores.
5. Detection results are stored in Amazon DynamoDB.
6. If suspicious objects are detected, Amazon SNS sends an alert.
7. Dashboard displays inspection results and history.

---

# 🚀 Deployment

The frontend is hosted on an Ubuntu EC2 instance using Apache Web Server.

The backend is deployed as AWS Lambda functions and exposed through Amazon API Gateway.

Uploaded images are securely stored in Amazon S3.

Amazon Rekognition analyzes uploaded images for object detection.

Detection records are stored in Amazon DynamoDB.

Amazon SNS sends security notifications.

Amazon CloudWatch monitors logs and system performance.

---

# 🔐 IAM Permissions

The Lambda execution role includes permissions for:

- rekognition:DetectLabels
- s3:GetObject
- s3:PutObject
- dynamodb:PutItem
- dynamodb:GetItem
- dynamodb:Scan
- sns:Publish
- logs:CreateLogGroup
- logs:CreateLogStream
- logs:PutLogEvents

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Airport-Security-System.git
```

Navigate to the project

```bash
cd Airport-Security-System
```

Deploy the frontend to Amazon EC2.

Create an Amazon S3 bucket for image storage.

Deploy the Lambda functions.

Create the DynamoDB table.

Configure Amazon Rekognition access.

Create Amazon SNS topic.

Create API Gateway endpoints.

Update API URLs inside `script.js`.

Launch the application.

---

# 🔮 Future Improvements

- Live CCTV Camera Integration
- Face Recognition for Watchlists
- Real-Time Video Analysis
- Weapon Detection using Custom Labels
- Security Officer Login
- Incident Reporting Dashboard
- Multi-Airport Support
- Analytics Dashboard
- PDF Inspection Reports
- SMS & Email Notifications
- AI-Based Threat Classification
- Mobile Application

---

# 👨‍💻 Author

**Pranav Chopade**


---

# ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub.
