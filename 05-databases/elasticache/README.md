# Amazon ElastiCache

## What is it?

Amazon ElastiCache is a fully managed in-memory caching service compatible with **Redis** and **Memcached**. It allows you to retrieve information from a fast, managed cache instead of relying entirely on slower disk-based databases — dramatically improving application performance.

## Use cases

- Caching results of heavy database queries
- User session storage
- Real-time leaderboards with Redis Sorted Sets
- API caching to reduce latency
- Pub/Sub messaging with Redis
- Work queues and real-time counters

## Key points for the exam (CLF-C02)

- **Redis vs Memcached:**
  - **Redis**: supports complex data structures (lists, sets, sorted sets, hashes), persistence, replication, Multi-AZ, pub/sub — more powerful and recommended
  - **Memcached**: simpler, multithreaded, basic key-value caching only — for simple use cases
- **In-memory**: data lives in RAM — much faster than disk (microseconds vs milliseconds)
- **Managed by AWS**: patching, backups, monitoring, automatic failover — no server management
- **Reduces database load**: applications query the cache first; only go to the database if the data is not in cache (cache miss)
- **Volatile**: in-memory data is lost if the node restarts (unless Redis persistence is used)
- **Typical pattern**: Application → ElastiCache → (on cache miss) → RDS/DynamoDB

## Practical example

**Scenario:** A news portal has a heavy query that generates the ranking of the top 10 most-read stories of the day — this query takes 2 seconds on RDS and runs 10,000 times per hour. With ElastiCache Redis, the query result is cached for 5 minutes. On the first execution, the query hits RDS (2s). On subsequent executions, the result comes from Redis in under 1ms. Database load drops by 99% and user experience improves significantly.
