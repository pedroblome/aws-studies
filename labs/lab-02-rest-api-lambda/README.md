# Lab 02 — Serverless REST API with Lambda and API Gateway

## What is it?

In this lab, you will learn how to build a completely serverless REST API using Amazon API Gateway as the HTTP frontend and AWS Lambda as the processing backend, with data stored in DynamoDB. This is the most common and widely used serverless architecture on AWS.

## Use cases

- Backends for mobile and web applications
- Serverless microservices
- Integration APIs between systems
- Webhook processing
- APIs with variable traffic (pay only for usage)

## Key points for the exam (CLF-C02)

- **API Gateway + Lambda**: the standard combination for serverless APIs on AWS
- **API Gateway**: manages authentication, throttling, caching, documentation, and request routing
- **Lambda**: processes requests without a server — scales from 0 to thousands of concurrent invocations
- **DynamoDB**: serverless NoSQL database — a natural complement to Lambda for storing data
- **No servers to manage**: all infrastructure is managed by AWS
- **Pay-per-use**: pay per request on API Gateway and per millisecond of execution on Lambda
- **IAM + API Keys + Cognito**: options for authenticating and authorizing API calls
- **CORS**: must be enabled on API Gateway for browser-based calls
- **Stages**: deployment environments in API Gateway (dev, staging, prod) with separate URLs

## Practical example

**Conceptual scenario — To-Do List API:**

**API endpoints:**
- `POST /tasks` → Lambda creates a new task in DynamoDB
- `GET /tasks` → Lambda lists all tasks from DynamoDB
- `GET /tasks/{id}` → Lambda fetches a task by ID
- `PUT /tasks/{id}` → Lambda updates a task
- `DELETE /tasks/{id}` → Lambda deletes a task

**Request flow:**
1. Mobile app sends `POST /tasks` with `{"title": "Study AWS"}` to API Gateway
2. API Gateway authenticates the request via API Key and validates the JSON
3. API Gateway invokes the Lambda function `CreateTask`
4. Lambda receives the event, generates a UUID, saves `{"id": "abc123", "title": "Study AWS", "done": false}` to DynamoDB
5. Lambda returns `{"statusCode": 201, "body": {"id": "abc123"}}`
6. API Gateway returns the response to the app with HTTP status 201

**Cost for 1 million requests/month**: approximately $3.50 (API Gateway) + $0.20 (Lambda) + minimal DynamoDB cost = less than $5/month total, with **zero** servers to manage.
