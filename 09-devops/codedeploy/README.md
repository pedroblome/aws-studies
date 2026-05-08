# AWS CodeDeploy

## What is it?

AWS CodeDeploy is a fully managed deployment service that automates application deployments to EC2 instances, on-premises servers, Lambda functions, and ECS services. It minimizes downtime during deployments and eliminates manual deployment errors.

## Use cases

- Automated application deployments to EC2 instances with zero downtime
- Lambda function updates with automatic validation
- Microservice deployments to ECS with blue/green deployment
- Deploying to on-premises servers as part of a hybrid strategy
- Automatic rollback in case of deployment failure

## Key points for the exam (CLF-C02)

- **Deployment strategies:**
  - **In-Place (Rolling)**: instances are updated one at a time or in groups — same environment, minimal downtime
  - **Blue/Green**: a new environment (green) is created with the new version; after validation, traffic is redirected from the old environment (blue) to the new one — no downtime
- **AppSpec file (appspec.yml)**: configuration file that defines how CodeDeploy should deploy — lifecycle hooks (BeforeInstall, AfterInstall, ApplicationStart, ValidateService)
- **Deployment Groups**: defines which instances/environments receive the deployment (via EC2 tags or Auto Scaling Groups)
- **Automatic rollback**: if health checks fail or CloudWatch alarms trigger, CodeDeploy automatically reverts
- **CodeDeploy Agent**: software installed on EC2/on-premises instances that executes the deployment commands
- **No agent required** for Lambda and ECS
- **Lifecycle hooks**: allow running custom scripts at each deployment phase (e.g., stop the service, take a backup, start)

## Practical example

**Scenario:** A team uses Blue/Green deployment for a critical API on EC2. CodeDeploy automatically creates a new Auto Scaling Group (green) with the new version of the application. Health check tests validate that the new version responds correctly. The Load Balancer is reconfigured to direct 100% of traffic to the green environment. If a CloudWatch alarm detects 500 errors above normal in the first 10 minutes, automatic rollback redirects traffic back to the blue environment in seconds — with NO downtime for users.
