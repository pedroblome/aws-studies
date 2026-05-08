# AWS X-Ray

## What is it?

AWS X-Ray is a distributed tracing service that helps you analyze and debug applications in production, especially distributed architectures and microservices. It lets you visualize the complete flow of a request through multiple services, identifying bottlenecks and errors.

## Use cases

- Debug performance issues in microservice applications
- Identify bottlenecks and latency in distributed architectures
- Trace requests end-to-end in serverless applications (Lambda + API Gateway)
- Analyze errors and exceptions in production with full context
- Understand how services communicate and where failures occur

## Key points for the exam (CLF-C02)

- **Distributed Tracing**: traces a request through multiple services, creating a visual map of the flow
- **Service Map**: graphical visualization of all services and how they connect — quickly identifies where errors or slowdowns occur
- **Traces and Segments**: a trace is the complete path of a request; each service adds a segment to the trace
- **X-Ray SDK**: application instrumentation via SDK (available for Python, Java, Node.js, .NET, Go, Ruby)
- **X-Ray Daemon**: process that collects and sends tracing data to the X-Ray service
- Integrates natively with: **Lambda, API Gateway, ECS, EC2, Elastic Beanstalk, SNS, SQS**
- **Sampling**: X-Ray does not trace 100% of requests by default — uses sampling to reduce cost and overhead
- **Annotations and Metadata**: add custom information to traces to facilitate analysis

## Practical example

**Scenario:** A checkout microservice is slow — users are complaining about payment delays. With X-Ray instrumented in the application, the team opens the Service Map and visualizes the flow: API Gateway → Lambda (checkout) → RDS (stock check) → external payment service. X-Ray shows the RDS call takes 2.8 seconds — far above normal. The team identifies a query missing an index and fixes the problem, reducing total time from 3.5 seconds to 180ms.
