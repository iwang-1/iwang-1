# Ivan Wang

**Software engineer focused on backend, distributed systems, and storage.**

[Portfolio](https://iwang-1.github.io/) · [LinkedIn](https://www.linkedin.com/in/ivanwang1) · [Email](mailto:ivanwang8989@gmail.com)

## Snapshot

- **AWS:** Software Development Engineer Intern, Summer 2026, working on agent-assisted test migration and EC2/VPC canary infrastructure.
- **University of Maryland:** Computer Science B.S./M.S., Departmental Honors research track, graduating May 2027.
- **Recruiting:** Seeking Summer 2027 new-grad software engineering roles, especially in backend, infrastructure, storage, and distributed systems.

## Featured Engineering

### [parallax-kv](https://github.com/iwang-1/parallax-kv) · Go, Raft, gRPC

A three-node Raft key-value store built from scratch with PreVote, ReadIndex, persist-before-send ordering, snapshots, and a durable write-ahead log.

- Deterministic stress testing exercises partitions, crashes, message loss, delays, and snapshots across 2.9 million client operations.
- The checker found zero safety or linearizability violations and helped expose a precision bug in the test harness itself.

### [accretion-db](https://github.com/iwang-1/accretion-db) · Rust, LSM tree, crash consistency

An embeddable storage engine with a CRC-framed WAL, group commit, memtables, block-based SSTables, bloom filters, and size-tiered compaction.

- Fault-injection and property-based tests verify that acknowledged writes survive simulated crashes.
- Safe Rust only, with roughly 29x WAL-bound throughput from group commit.

## Selected Work

- **[UMD Observatory CCD Data Archive](https://github.com/warnerem/CCD-data-archive):** Python, Flask, and SQLite application serving 50,000+ astronomy records; optimized ingestion and query paths to reduce pipeline runtime by 75%.
- **[Cross-Domain Sentiment DANN](https://github.com/iwang-1/cross-domain-sentiment-dann):** DistilBERT and domain-adversarial training across Yelp, Amazon, Twitter, and Reddit, with explicit evidence boundaries and reproducible workflows.
- **[Quantum NLP Research](https://github.com/iwang-1/FIRE-QML-WINNERS-QNLP):** Four-person research artifact using DisCoPy, Qiskit, pytket, and JAX; I worked on dataset preparation, experiment integration, and documentation.
- **[Portfolio](https://github.com/iwang-1/iwang-1.github.io):** React and TypeScript site with static prerendering, no-JavaScript fallbacks, factual guardrails, accessibility checks, and Playwright verification.

## Technical Focus

**Languages:** Go · Rust · Java · Python · TypeScript/JavaScript · SQL · Bash

**Backend and systems:** Raft · gRPC/Protobuf · LSM trees · PostgreSQL/SQLite · Flask/FastAPI · JUnit 5

**Infrastructure:** AWS · Docker · Linux · GitHub Actions · Jenkins · Playwright

**ML and research:** PyTorch · Hugging Face · scikit-learn · Qiskit · DisCoPy · JAX

## Beyond Code

I serve as Secretary of the UMD Climbing Club, organizing eight trips each semester and helping grow attendance by 30%. I also build mechanical keyboards and custom PCs.

## Contact

The fastest way to reach me is [email](mailto:ivanwang8989@gmail.com). You can also find my complete project and experience overview at [iwang-1.github.io](https://iwang-1.github.io/).
