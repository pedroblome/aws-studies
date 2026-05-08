# AWS CodePipeline

## What is it?

AWS CodePipeline is a fully managed continuous delivery (CD) service that automates release pipelines for fast and reliable application updates. It orchestrates the build, test, and deploy steps whenever a change occurs in the source code.

## Use cases

- Automate the build → test → deploy flow for applications
- Implement CI/CD for applications on EC2, ECS, Lambda, or on-premises
- Orchestrate multiple development tools (CodeCommit, GitHub, CodeBuild, CodeDeploy)
- Implement manual approval gates before deploying to production
- Standardize the software delivery process across the organization

## Key points for the exam (CLF-C02)

- **Pipeline**: sequence of stages that code goes through from commit to deploy
- **Stages**: steps of the pipeline — typically Source → Build → Test → Deploy
- **Actions**: actions within each stage (e.g., check code from GitHub, run CodeBuild, deploy with CodeDeploy)
- **Integration**: works with CodeCommit, GitHub, Bitbucket (Source); CodeBuild (Build); CodeDeploy, ECS, Lambda, CloudFormation (Deploy)
- **Notifications**: integrates with SNS and CloudWatch Events for alerts on failures and approvals
- **Manual approval**: add an approval stage to require human review before deploying to production
- **Parallel actions**: actions within the same stage can execute in parallel
- **Fully managed and serverless**: no servers to manage; pay per active pipeline per month

## Practical example

**Scenario:** A dev team uses GitHub for version control. CodePipeline monitors the `main` branch: when a PR is merged, the pipeline triggers automatically — (1) Source: clones the code from GitHub; (2) Build: CodeBuild runs unit tests and produces the artifact; (3) Deploy-Staging: CodeDeploy deploys to the staging environment; (4) Manual approval: the tech lead approves the deploy; (5) Deploy-Prod: CodeDeploy deploys to production with a rolling update. The entire process is audited and repeatable.
