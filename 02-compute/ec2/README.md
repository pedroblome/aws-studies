# Amazon EC2 (Elastic Compute Cloud)

## What is it?

Amazon EC2 is AWS's virtual computing service that provides servers (instances) in the cloud. You choose the instance type (CPU, memory, storage), the operating system, and pay only for the time you use it. It is the foundation of AWS compute infrastructure.

## Use cases

- Host web applications and backend APIs
- Run database servers
- Process large volumes of data (big data, machine learning)
- Development and testing environments
- Host legacy applications that require full server control

## Key points for the exam (CLF-C02)

- **Pricing models:**
  - **On-Demand**: pay for what you use, no commitment — ideal for unpredictable workloads
  - **Reserved Instances**: up to 72% discount with a 1 or 3-year commitment
  - **Spot Instances**: up to 90% cheaper, but AWS can interrupt them — ideal for fault-tolerant workloads
  - **Savings Plans**: similar discount to Reserved, with more usage flexibility
  - **Dedicated Hosts**: dedicated physical server — for compliance or software licensing requirements
- **Instance types:** General Purpose (T, M), Compute Optimized (C), Memory Optimized (R, X), Storage Optimized (I, D)
- **EC2 is an IaaS service** (Infrastructure as a Service) — you manage the OS and above
- **Auto Scaling** automatically scales the number of instances based on demand
- **Elastic Load Balancer (ELB)** distributes traffic across multiple instances
- **Security Groups** act as a virtual firewall at the instance level

## Practical example

**Scenario:** An online store has traffic spikes during Black Friday. The architect configures an Auto Scaling Group with `t3.medium` EC2 instances (On-Demand for the minimum) and Spot Instances to absorb the peaks — saving up to 70% on extra costs. An Application Load Balancer distributes requests across instances, and CloudWatch monitors CPU to trigger scaling automatically.
