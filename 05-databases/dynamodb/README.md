# Amazon DynamoDB

## What is it?

Amazon DynamoDB is a fully managed, serverless NoSQL database with high performance and unlimited scalability. It offers single-digit millisecond latency at any scale — from a few items to trillions of records and petabytes of data.

## Use cases

- Shopping cart and user sessions in e-commerce
- Product catalogs with variable attributes
- Gaming data (leaderboards, player profiles)
- IoT — real-time ingestion of sensor data
- Serverless applications with Lambda (a natural combination)
- Application data and metadata caching

## Key points for the exam (CLF-C02)

- **NoSQL**: stores data as documents or key-value pairs — no fixed schema (schema-less)
- **Serverless**: no servers to manage — capacity scales automatically
- **Capacity modes:**
  - **On-Demand**: pay per request — ideal for unpredictable traffic
  - **Provisioned**: define RCUs and WCUs — cheaper with predictable traffic
- **Primary Key**: composed of a **Partition Key** (required) + **Sort Key** (optional)
- **DynamoDB Streams**: captures data changes in real time — ideal for triggering Lambda
- **DAX (DynamoDB Accelerator)**: in-memory cache for DynamoDB — reduces latency from milliseconds to microseconds
- **Global Tables**: fully managed multi-region replication — low-latency global access
- **Different from RDS**: does not support SQL, joins, or traditional complex transactions — but far more scalable and faster for simple access patterns
- Automatic replication across multiple AZs — highly available by default

## Practical example

**Scenario:** A ride-sharing app needs to store the real-time location of 500,000 drivers, updated every 5 seconds. A relational database could not handle the load. With DynamoDB On-Demand, each location update is a `PutItem` operation with the driver's ID as the partition key. DynamoDB automatically scales to absorb 500,000 writes per second and reads any driver's location in under 1ms — with no servers to manage.
