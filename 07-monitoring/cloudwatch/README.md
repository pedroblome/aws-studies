# Amazon CloudWatch

## What is it?

Amazon CloudWatch is AWS's monitoring and observability service. It collects and tracks metrics, collects and monitors log files, sets alarms, and automatically reacts to changes in AWS resources. It is the central observability tool for applications and infrastructure on AWS.

## Use cases

- Monitor CPU, memory, and disk utilization of EC2 instances
- Create alarms that send notifications (via SNS) when metrics exceed thresholds
- Centralize and analyze logs from applications and AWS services
- Trigger automatic actions (Auto Scaling, Lambda) based on metrics
- Create dashboards for real-time visualization of system health
- Monitor costs and usage of AWS services

## Key points for the exam (CLF-C02)

- **Metrics**: numerical data collected over time (CPU, NetworkIn, RequestCount, etc.)
  - Default EC2 metrics: CPU, network, disk — every 5 minutes
  - **Detailed Monitoring**: metrics every 1 minute (additional cost)
  - **Custom Metrics**: your own metrics (e.g., active users, queue size)
- **Logs**: CloudWatch Logs centralizes logs from applications, Lambda, RDS, VPC Flow Logs, etc.
  - **Log Groups**: containers for related logs
  - **Log Insights**: SQL-like queries to analyze logs
- **Alarms**: monitor a metric and trigger actions when it exceeds a threshold
  - States: OK, ALARM, INSUFFICIENT_DATA
  - Actions: notify via SNS, trigger Auto Scaling, execute EC2 action
- **Dashboards**: customizable visualization panels with metric graphs
- **EventBridge (CloudWatch Events)**: trigger actions based on events or schedules
- **Metric retention**: 15 months for standard metrics

## Practical example

**Scenario:** A DevOps team configures CloudWatch to monitor their production application: an alarm fires when CPU on any EC2 instance exceeds 80% for 5 minutes — SNS sends an email notification and triggers Auto Scaling to add instances. Nginx logs are sent to CloudWatch Logs and Log Insights is used to query 500 errors in real time. A dashboard shows key application metrics on a single panel.
