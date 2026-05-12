# Amazon Kinesis

## What is it?

Amazon Kinesis is a platform for real-time streaming data on AWS. It enables you to collect, process, and analyze data streams in real time — think millions of events per second from IoT sensors, application logs, clickstreams, financial transactions, and more.

Unlike SQS (a queue for discrete tasks) or EventBridge (an event router), Kinesis is purpose-built for **continuous, high-volume data streams** where every record matters and you need to process data within milliseconds of it arriving.

## Kinesis Family

| Service | Purpose |
|---|---|
| **Kinesis Data Streams (KDS)** | Core streaming service — ingest, store, and process real-time data |
| **Kinesis Data Firehose** | Fully managed delivery of streams to S3, Redshift, OpenSearch, Splunk |
| **Kinesis Data Analytics** | Run SQL or Apache Flink on streaming data without managing infrastructure |
| **Kinesis Video Streams** | Stream video from devices for ML and analytics |

> For the SAA-C03 exam, focus on **Kinesis Data Streams** and **Kinesis Data Firehose**.

---

## Kinesis Data Streams (KDS)

### How it works

```
[Producers]              [KDS]                  [Consumers]
App servers   →    Shard 1 (1 MB/s in)   →    Lambda
IoT devices        Shard 2 (1 MB/s in)   →    KCL App (EC2)
Mobile apps        Shard 3 (1 MB/s in)   →    Kinesis Data Analytics
Click events                                   Kinesis Firehose
```

A **stream** is composed of one or more **shards**. Each shard provides:
- **1 MB/s input** (1,000 records/s)
- **2 MB/s output** per consumer
- Records are stored for **1 to 365 days** (default: 24h) — enabling replay

Producers write records to a shard using a **partition key**. Records with the same partition key always go to the same shard — this guarantees ordering per partition key.

### Key concepts

- **Shard**: the base throughput unit. Scale by adding more shards (shard splitting) or reducing (shard merging).
- **Partition Key**: determines which shard a record goes to. Choose a high-cardinality key (e.g., user ID, device ID) to distribute load evenly across shards — a bad partition key creates a "hot shard".
- **Sequence Number**: unique ID assigned to each record within a shard — used for ordered replay.
- **Retention Period**: records persist in the stream from 24 hours (default) up to 365 days. This is the killer feature vs. SQS — you can re-process old data.
- **Enhanced Fan-Out**: each registered consumer gets its own dedicated 2 MB/s read throughput per shard using HTTP/2 push — no need to share the default 2 MB/s limit across all consumers.
- **Checkpointing**: consumers track their position in the stream (a checkpoint) so they can resume from where they left off after a restart.

### Capacity modes

| Mode | How it works | Best for |
|---|---|---|
| **Provisioned** | You manually set the number of shards; pay per shard-hour | Predictable, steady traffic |
| **On-Demand** | AWS auto-scales capacity; pay per GB ingested/retrieved | Variable or unknown traffic |

---

## Kinesis Data Firehose

The easiest way to load streaming data into data stores. Firehose is **fully managed with zero administration** — no shards, no consumers to manage.

```
[Producers / KDS]  →  [Firehose]  →  buffer + (optional transform via Lambda)  →  [Destination]
```

**Destinations:**
- Amazon S3 (most common)
- Amazon Redshift (via S3 intermediate)
- Amazon OpenSearch Service
- Splunk, Datadog, New Relic, MongoDB (HTTP endpoint)

**Key features:**
- **Near-real-time** (60s minimum buffer, or 1–128 MB buffer size)
- **Automatic compression** (GZIP, Snappy, ZIP)
- **Optional transformation** via Lambda (e.g., parse logs, enrich records)
- **No replay** — Firehose is a one-way delivery pipe, not a storage layer

---

## When to use each Kinesis service

| Scenario | Use |
|---|---|
| Real-time processing, custom consumers, replay needed | Kinesis Data Streams |
| Load data into S3/Redshift/OpenSearch, near real-time is fine | Kinesis Firehose |
| SQL analytics on a live stream | Kinesis Data Analytics |
| Video streaming from cameras / devices | Kinesis Video Streams |

## SQS vs Kinesis Data Streams

| Feature | SQS | Kinesis Data Streams |
|---|---|---|
| Consumption model | Pull, message deleted after consumption | Pull, record persists in stream |
| Multiple consumers | One consumer group per queue | Multiple independent consumers |
| Ordering | FIFO queues only | Per shard (partition key) |
| Replay | No — once consumed and deleted, gone | Yes — up to 365 days |
| Throughput | Nearly unlimited (Standard) | 1 MB/s per shard |
| Use case | Task/work queues | Real-time analytics, event sourcing |
| Scaling unit | Automatic | Manual (shards) or on-demand |

**Rule of thumb:** If you need to send a "job" to one worker → **SQS**. If you need to stream continuous data to multiple analytics consumers with replay capability → **Kinesis Data Streams**.

## Key points for the exam (CLF-C02 / SAA-C03)

- **KDS**: real-time, multiple consumers, replay — provision shards (1 MB/s in, 2 MB/s out each)
- **Firehose**: fully managed delivery to S3, Redshift, OpenSearch, Splunk — near real-time (minimum 60s buffer), no replay
- A **hot shard** happens when too many records share the same partition key — fix by choosing a high-cardinality key
- **Enhanced Fan-Out** gives each consumer dedicated 2 MB/s per shard — use when multiple Lambda functions or KCL apps need full throughput
- Kinesis **retains data** (vs. SQS which deletes after consumption) — this enables event sourcing and re-processing
- Lambda can be a consumer of KDS — it polls the stream and processes batches of records

## Practical example

**Scenario — Real-time e-commerce analytics:**

An e-commerce platform captures every user action: page views, product clicks, add-to-cart, and purchases. These events flow from the web/mobile frontend at up to 100,000 events/second.

```
[Web/Mobile App]
      ↓  PutRecord (partition key = user_id)
[Kinesis Data Streams — 10 shards]
      ├──→ Lambda: real-time fraud detection (flag suspicious purchase patterns)
      ├──→ Kinesis Data Analytics: live dashboard (items/s, revenue/min, top products)
      └──→ Kinesis Firehose → S3 (Parquet) → Athena / Redshift for daily reporting
```

- **Lambda** reacts within milliseconds to flag fraud
- **Data Analytics** runs a sliding-window SQL query: "purchases per minute over the last 5 minutes"
- **Firehose** archives every event to S3 in Parquet format for cheap historical analysis
- If the fraud detection Lambda has a bug, you **replay** the last 24 hours of the stream after the fix — no data was lost

This architecture is impossible with SQS (no multi-consumer replay) and inadequate with EventBridge (not designed for millions of events/second from a single application).
