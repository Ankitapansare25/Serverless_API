# 🚀 Serverless API Deployment using Terraform & Jenkins CI/CD

## 📌 Project Overview

This project demonstrates automated deployment of a Serverless API using:

- AWS Lambda
- API Gateway
- S3 (for Lambda artifact storage)
- Terraform (Infrastructure as Code)
- Jenkins CI/CD Pipeline
- AWS CLI

The Lambda function is packaged, uploaded to S3, and deployed using Terraform.  
Jenkins automates the entire process including API validation.

---

## 🏗️ Architecture Overview

This project provisions the following AWS resources:

- AWS Lambda Function
- API Gateway (REST API)
- S3 Bucket (to store Lambda zip file)
- IAM Roles & Permissions (for Lambda execution)

Terraform manages all infrastructure components.

---

## 🔄 CI/CD Pipeline Flow

### Step 1: Source Code Checkout
Jenkins pulls the latest code from the GitHub repository.

### Step 2: Package Lambda Function
The Lambda function file (`lambda_function.py`) is zipped:

```
zip -r lambda_function.zip lambda_function.py
```

### Step 3: Upload Artifact to S3
The zipped Lambda package is uploaded to the configured S3 bucket using AWS CLI:

```
aws s3 cp lambda_function.zip s3://<bucket-name>/
```

### Step 4: Provision Infrastructure using Terraform
Inside the `terraform` directory:

```
terraform init
terraform apply -auto-approve
```

Terraform:
- Creates/updates Lambda function
- Configures API Gateway
- Connects API Gateway to Lambda
- Outputs the API endpoint URL

### Step 5: API Validation (Automated Testing)

Jenkins fetches the API URL from Terraform output:

```
terraform output -raw api_url
```

Then performs automated testing using `curl`:

- GET request
- POST request
- DELETE request

If API responds correctly, pipeline is marked as SUCCESS.

---

## 🛠️ Tech Stack

### 🌍 Infrastructure
- Terraform
- AWS Lambda
- API Gateway
- S3
- IAM

### ⚙️ CI/CD
- Jenkins
- GitHub
- AWS CLI

### 💻 Application
- Python (Lambda function)

---

## 📦 Terraform Commands Used

```
terraform init
terraform plan
terraform apply
terraform destroy
```

---

## 🌐 API Endpoint

After successful deployment, Terraform outputs:

```
https://<api-id>.execute-api.ap-south-1.amazonaws.com/<stage>
```

---

## 🎯 Key Learning Outcomes

- Serverless architecture implementation
- Lambda deployment automation
- API Gateway integration
- Terraform Infrastructure as Code
- Artifact upload using AWS CLI
- Jenkins CI/CD automation
- Automated API testing inside pipeline

---

## 👩‍💻 Author

Ankita Pansare  

---
