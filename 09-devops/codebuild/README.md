# AWS CodeBuild

## What is it?

AWS CodeBuild is a fully managed continuous integration (CI) service that compiles source code, runs tests, and produces software packages ready for deployment. It is serverless — you do not need to provision, manage, or scale build servers.

## Use cases

- Compile Java, .NET, Python, Node.js, Go, and other code
- Automatically run unit and integration tests
- Build Docker images and publish them to ECR
- Run static code analysis (SAST) and security checks
- Generate deployment artifacts (JARs, ZIPs, npm packages)

## Key points for the exam (CLF-C02)

- **Serverless**: no build servers to provision — CodeBuild scales automatically with demand
- **buildspec.yml**: YAML file in the repository that defines the build commands — phases: install, pre_build, build, post_build
- **Build environments**: pre-configured build environments (Ubuntu, Amazon Linux) with common tools — or custom Docker images
- **Per-minute billing**: pay only for the compute time used in builds — no costs when no builds are running
- **Integration**: works natively with CodePipeline, CodeCommit, GitHub, Bitbucket, S3, ECR
- **Test reports**: integrates with testing frameworks (JUnit, pytest) to display results in the console
- **Cache**: stores dependencies in cache (S3 or local) to speed up subsequent builds
- **Environment variables**: supports environment variables and integration with Secrets Manager/SSM Parameter Store for sensitive data

## Practical example

**Scenario:** A Spring Boot application uses CodeBuild with the following `buildspec.yml`: the `install` phase installs Java 17; the `build` phase runs `mvn package` — compiles the code and runs 300 unit tests; the `post_build` phase builds a Docker image and pushes it to ECR. If any test fails, the build is marked as failed and CodePipeline stops — preventing code with errors from reaching production. The entire process takes 4 minutes and the team pays only for those 4 minutes of compute time.
