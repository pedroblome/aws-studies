# Amazon ECR (Elastic Container Registry)

## What is it?

Amazon ECR is a fully managed Docker container registry that makes it easy to store, manage, and deploy container images. It eliminates the need to operate your own registry infrastructure or worry about the scalability of image storage.

## Use cases

- Store and version Docker images for deployment on ECS, EKS, or EC2
- CI/CD pipeline: CodeBuild builds the image and pushes it to ECR; CodeDeploy/ECS pulls it for deployment
- Securely share container images between AWS accounts
- Scan images for vulnerabilities before deployment
- Store company-specific custom base images

## Key points for the exam (CLF-C02)

- **Repositories**: containers for images — can be public (ECR Public Gallery) or private
- **Native integration**: works seamlessly with ECS, EKS, CodeBuild, CodeDeploy, and other AWS services
- **IAM authentication**: granular access control using IAM policies — no separate credentials needed
- **Image Scanning**: automatic vulnerability scanning using the CVE database — identifies security issues before deployment
- **Lifecycle Policies**: rules to automatically delete old images (e.g., keep only the last 10 versions) — cost control
- **Tag immutability**: option to prevent a tag from being overwritten (e.g., ensuring `v1.0.0` always points to the same image)
- **Replication**: automatically replicates images to multiple regions — for multi-region deployments
- **ECR Public Gallery**: public repository for sharing images with anyone (similar to Docker Hub)

## Practical example

**Scenario:** A complete CI/CD pipeline using AWS tools: a developer pushes to CodeCommit → CodePipeline triggers → CodeBuild compiles and builds the Docker image → pushes to ECR with the version tag (e.g., `my-app:v2.3.1`) → ECR scans the image and finds no critical vulnerabilities → ECS pulls the new image from ECR and deploys with a rolling update. Everything runs within the private AWS network — no traffic goes through the public internet.
