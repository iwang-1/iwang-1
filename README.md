# Ivan Wang

**UMD computer science B.S./M.S.**, Departmental Honors research track, graduating May 2027.<br>
**SDE intern at AWS** on EC2 Networking, Summer 2026.

Open to Summer 2027 internships and new-grad roles, relocating anywhere in the US.

[Portfolio](https://iwang-1.github.io/) · [LinkedIn](https://www.linkedin.com/in/ivanwang1) · [ivanwang8989@gmail.com](mailto:ivanwang8989@gmail.com)

## At AWS, Summer 2026

On EC2 Networking, I built an autonomous Claude Code agent with custom skills that migrated seven production EC2/VPC canaries from Scala to Java and JUnit 5, reducing per-test migration from about one week to about one day, gated on live integration testing.

## What I built

Three systems written from scratch, each measured against a committed benchmark file.

### [parallax-kv](https://github.com/iwang-1/parallax-kv) — linearizable key-value store, Go

Raft consensus from scratch: PreVote, ReadIndex linearizable reads, persist-before-send ordering, snapshots, a durable write-ahead log, and a gRPC runtime.

> A deterministic harness replayed partitions, crashes, message loss, delays, and snapshot churn across **2.9M client operations** — zero safety or linearizability violations. The first bug it caught was in my own election-safety check, not in the consensus code.
>
> <sub>[docs/BUG_LEDGER.md](https://github.com/iwang-1/parallax-kv/blob/main/docs/BUG_LEDGER.md) · 3 nodes, 6 simulated clients, virtual time · not built: production snapshot scheduling or chunked streaming</sub>

### [accretion-db](https://github.com/iwang-1/accretion-db) — crash-safe LSM storage engine, Rust

A CRC-framed write-ahead log with group commit, memtables, block-based SSTables with bloom filters, and size-tiered compaction. `unsafe` is forbidden at the crate root, so the engine has no unsafe blocks by construction.

> A fault-injecting storage layer replays power loss at **330 deterministic crash points** (2,640 executions) plus 160 property-based crash schedules: **zero acknowledged-write loss**, and a **~29x** gain from group commit.
>
> <sub>[benchmarks/RESULTS.md](https://github.com/iwang-1/accretion-db/blob/main/benchmarks/RESULTS.md) · 16-byte keys, 100-byte values, ext4 on NVMe · compared against sled, including the cases sled wins · the ~29x is WAL-bound, and compaction runs under the write lock</sub>

### [lodestone](https://github.com/iwang-1/lodestone) — vector search engine, Rust

An HNSW proximity graph and an IVF-PQ compressed index over hand-written AVX-512 distance kernels with runtime feature dispatch, for embeddings and RAG retrieval.

> On 50,000 128-dimensional vectors on a single core, HNSW reached **0.976 recall@10 at about 31,800 queries per second** — about **33x** the exact brute-force search at that recall, and **9–33x** across the 90%+ recall band. IVF-PQ holds 0.975 recall@10 at 16x memory compression.
>
> <sub>[benchmarks/raw/bench_50k_128d.txt](https://github.com/iwang-1/lodestone/blob/main/benchmarks/raw/bench_50k_128d.txt) · single machine, single core, Xeon 8488C · not built: distributed sharding</sub>

## Upstream and research

**Four merged pull requests** to the [UMD Observatory data archive](https://github.com/warnerem/CCD-data-archive/pulls?q=is%3Apr+author%3Aiwang-1+is%3Amerged) — Python, Flask, SQLite, 50,000+ records.

**Co-built and open-sourced** a [four-person quantum-NLP research artifact](https://github.com/iwang-1/FIRE-QML-WINNERS-QNLP) — DisCoPy, Qiskit, pytket, JAX. My part was dataset preparation, experiment integration, and documentation.

**One pull request open and under review**: [lambeq #259](https://github.com/Quantinuum/lambeq/pull/259) adds a `LAMBEQ_MODELS_URL` override for model downloads.

## Toolbox

**Languages** — Python · Java · Go · Rust · TypeScript/JavaScript · Scala · SQL · Bash<br>
**Distributed & storage** — Raft · gRPC/Protobuf · LSM trees · PostgreSQL/SQLite<br>
**Backend, web & testing** — Flask/FastAPI · Node.js · JUnit 5 · Playwright<br>
**ML & NLP** — PyTorch · HuggingFace · scikit-learn · LangChain · JAX · Qiskit · DisCoPy · pytket<br>
**Cloud & CI** — AWS (EC2/VPC, SDK, CDK, CloudWatch) · Docker · Linux · GitHub Actions · CI/CD · Jenkins

## Contact

[ivanwang8989@gmail.com](mailto:ivanwang8989@gmail.com) · [LinkedIn](https://www.linkedin.com/in/ivanwang1) · [more work on the portfolio](https://iwang-1.github.io/projects/)

<sub>Resume on request.</sub>
