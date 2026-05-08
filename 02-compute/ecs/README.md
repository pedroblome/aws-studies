# Amazon ECS (Elastic Container Service)

## What is it?

Amazon ECS is a fully managed container orchestration service that allows you to run, scale, and manage Docker container applications on AWS. ECS eliminates the need to install and operate your own container orchestration infrastructure.

## Use cases

- Run microservices in Docker containers
- Migrate monolithic applications to a microservices architecture
- CI/CD pipelines that deploy container images
- Batch processing with containers
- Highly scalable web applications in containers

## Key points for the exam (CLF-C02)

- **Two launch types:**
  - **EC2 Launch Type**: you manage the EC2 instances that host the containers
  - **Fargate Launch Type**: **serverless** — AWS manages the underlying infrastructure; you only define CPU/memory for the container
- **Natively integrates** with ECR (image registry), Load Balancer, IAM, and CloudWatch
- **Task Definition**: defines how a container should run (image, CPU, memory, environment variables)
- **Service**: ensures a specific number of tasks are always running
- **ECS vs EKS**: ECS is simpler and AWS-integrated; EKS uses Kubernetes and is more complex but more portable
- Fargate is the **serverless** option for containers — eliminates server management

## Practical example

**Scenario:** A fintech has a REST API packaged in Docker. With ECS + Fargate, the team deploys the image from ECR without worrying about servers. An Application Load Balancer distributes traffic, and the ECS Service ensures 3 tasks are always running. When CloudWatch detects a CPU spike, ECS Auto Scaling launches new tasks automatically — all without managing any EC2 instances.
