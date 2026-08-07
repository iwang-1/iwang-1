<div align="center">

<img width="100%" alt="Ivan Wang, Software Engineer" src="https://capsule-render.vercel.app/api?type=waving&color=0:1C1B18,50:1E4B7A,100:A6431E&height=200&section=header&text=Ivan%20Wang&fontSize=60&fontColor=F5F2EC&animation=fadeIn&fontAlignY=36&desc=Software%20Engineer&descSize=18&descAlignY=57">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://readme-typing-svg.demolab.com/?font=Fira+Code&weight=600&size=19&pause=1200&color=7FB3E0&center=true&vCenter=true&width=700&height=44&lines=I+like+taking+things+apart+to+see+how+they+work;then+building+my+own;SDE+intern+at+AWS%2C+summer+2026;CS+B.S.%2FM.S.+at+UMD+%E2%80%94+graduating+May+2027;Open+to+Summer+2027+internships+and+new-grad+roles">
  <img alt="I like taking things apart to see how they work, then building my own. SDE intern at AWS, summer 2026. CS B.S./M.S. at UMD, graduating May 2027. Open to Summer 2027 internships and new-grad roles." src="https://readme-typing-svg.demolab.com/?font=Fira+Code&weight=600&size=19&pause=1200&color=1E4B7A&center=true&vCenter=true&width=700&height=44&lines=I+like+taking+things+apart+to+see+how+they+work;then+building+my+own;SDE+intern+at+AWS%2C+summer+2026;CS+B.S.%2FM.S.+at+UMD+%E2%80%94+graduating+May+2027;Open+to+Summer+2027+internships+and+new-grad+roles">
</picture>

<p>
  <img alt="AWS SDE Intern, Summer 2026" src="https://img.shields.io/badge/AWS-SDE_Intern_·_Summer_2026-FF9900?style=for-the-badge&logo=amazonwebservices&logoColor=white">
  <img alt="UMD Computer Science B.S./M.S., May 2027" src="https://img.shields.io/badge/UMD-CS_B.S.%2FM.S._·_May_2027-1C1B18?style=for-the-badge">
  <img alt="Open to Summer 2027 internships and new-grad roles" src="https://img.shields.io/badge/Open_to-Summer_2027_·_new_grad-1E4B7A?style=for-the-badge">
</p>
<p>
  <a href="https://iwang-1.github.io/"><img alt="Portfolio: iwang-1.github.io" src="https://img.shields.io/badge/Portfolio-iwang--1.github.io-A6431E?style=for-the-badge&logo=githubpages&logoColor=white"></a>
  <a href="https://www.linkedin.com/in/ivanwang1"><img alt="LinkedIn: ivanwang1" src="https://img.shields.io/badge/LinkedIn-ivanwang1-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"></a>
  <a href="mailto:ivanwang8989@gmail.com"><img alt="Email: ivanwang8989@gmail.com" src="https://img.shields.io/badge/Email-ivanwang8989@gmail.com-64625E?style=for-the-badge&logo=maildotru&logoColor=white"></a>
</p>

</div>

## 👋 About

I mostly build things to find out how they work. Lately that has meant **three systems
written from scratch**: a Raft key-value store, an LSM storage engine, and a vector search
engine. For each one I wrote the test harness before the thing it was meant to judge.

I'm an **SDE intern at AWS** on EC2 Networking this summer, finishing a **CS B.S./M.S. at
UMD** on the Departmental Honors research track, and **open to Summer 2027 internships and
new-grad roles**. I'll relocate anywhere in the US.

Every number below comes from a benchmark committed in the repo it describes, so you can
re-run it yourself. Where a result is worse than what I compared against, it's published
anyway.

Outside of work I'm into **mechanical keyboards**: you can customize every part, and
picking the right one for the job is the fun of it. I also boulder, where a problem can
usually be done a lot of different ways, and working out which one costs you the least is
my favorite part. And I keep up with where the industry is heading, from new hardware to
how governments are handling AI.

<img width="100%" height="4" alt="" src="https://capsule-render.vercel.app/api?type=rect&color=0:1C1B18,50:1E4B7A,100:A6431E&height=4">

## 🚀 What I built

<table>
<tr>
<td width="50%" valign="top">

### 🧭 [parallax-kv](https://github.com/iwang-1/parallax-kv)
**Linearizable key-value store · Go**

Raft from scratch: PreVote, ReadIndex linearizable reads, persist-before-send ordering,
snapshots, a durable WAL, and a gRPC runtime.

> A deterministic harness replayed partitions, crashes, message loss, delays and snapshot
> churn across **2.9M client operations**: zero safety violations, and zero `Illegal`
> verdicts from the linearizability checker. The first bug it caught was in my own
> election-safety check, not in the consensus code.

![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![Raft](https://img.shields.io/badge/Raft-1E4B7A?style=flat-square)
![gRPC](https://img.shields.io/badge/gRPC-64625E?style=flat-square&logo=grpc&logoColor=white)
![Porcupine](https://img.shields.io/badge/Porcupine-A6431E?style=flat-square)

</td>
<td width="50%" valign="top">

### 💾 [accretion-db](https://github.com/iwang-1/accretion-db)
**Crash-safe LSM storage engine · Rust**

A CRC-framed write-ahead log with group commit, memtables, block SSTables with bloom
filters, and size-tiered compaction. `unsafe` is forbidden at the crate root, so the
engine has no unsafe blocks by construction.

> Power loss is replayed at **330 deterministic crash points** (2,640 executions) plus 160
> property-based schedules: **zero acknowledged-write loss**, and a **~29x** gain from
> group commit. Benchmarked against sled, which wins every matched comparison on this
> host. Reported rather than omitted.

![Rust](https://img.shields.io/badge/Rust-CE422B?style=flat-square&logo=rust&logoColor=white)
![LSM tree](https://img.shields.io/badge/LSM_tree-1E4B7A?style=flat-square)
![group commit](https://img.shields.io/badge/group_commit-64625E?style=flat-square)
![proptest](https://img.shields.io/badge/proptest-A6431E?style=flat-square)

</td>
</tr>
<tr><td colspan="2"></td></tr>
<tr>
<td width="50%" valign="top">

### 🧲 [lodestone](https://github.com/iwang-1/lodestone)
**Vector search engine · Rust**

An HNSW proximity graph and an IVF-PQ compressed index over hand-written AVX-512 distance
kernels with runtime feature dispatch, for embeddings and RAG retrieval.

> On 50,000 128-dimensional vectors on one core, HNSW reached **0.976 recall@10 at about
> 31,800 queries per second**, about **33x** the exact brute-force search at that recall,
> and **9–33x** across the 90%+ recall band. The honest catch: that baseline runs in
> parallel across all 48 vCPU while the search runs on one, so the two sides of the ratio
> aren't core-for-core.

![Rust](https://img.shields.io/badge/Rust-CE422B?style=flat-square&logo=rust&logoColor=white)
![HNSW](https://img.shields.io/badge/HNSW-1E4B7A?style=flat-square)
![IVF-PQ](https://img.shields.io/badge/IVF--PQ-64625E?style=flat-square)
![AVX-512](https://img.shields.io/badge/AVX--512_SIMD-A6431E?style=flat-square)

</td>
<td width="50%" valign="top">

### 🌍 Upstream & research

![4 merged](https://img.shields.io/badge/merged-×4-2ea043?style=flat-square&logo=git&logoColor=white) **[CCD-data-archive](https://github.com/warnerem/CCD-data-archive/pulls?q=is%3Apr+author%3Aiwang-1+is%3Amerged)**

Four merged pull requests to the UMD Observatory data archive, in Python, Flask and SQLite,
50,000+ records.

![open](https://img.shields.io/badge/open-under_review-d29922?style=flat-square) **[lambeq #259](https://github.com/Quantinuum/lambeq/pull/259)**

One pull request open upstream, adding a `LAMBEQ_MODELS_URL` override for model downloads.

![research](https://img.shields.io/badge/research-1E4B7A?style=flat-square) **[Quantum NLP (FIRE)](https://github.com/iwang-1/FIRE-QML-WINNERS-QNLP)**

A four-person research project, co-built and open-sourced, in DisCoPy, Qiskit, pytket and JAX.
My part was dataset preparation, experiment integration, and documentation.

<sub>The ML, NLP and statistics work is on the
<a href="https://iwang-1.github.io/projects/">portfolio</a> ↗</sub>

</td>
</tr>
</table>

<img width="100%" height="4" alt="" src="https://capsule-render.vercel.app/api?type=rect&color=0:A6431E,50:1E4B7A,100:1C1B18&height=4">

## 🧰 What I work in

**Languages** · Python · Java · Go · Rust · TypeScript/JavaScript · Scala · SQL · Bash

**Systems, backend & testing** · Raft · gRPC/Protobuf · LSM trees · PostgreSQL/SQLite ·
Flask/FastAPI · Node.js · JUnit 5 · Playwright

**ML, NLP & research** · PyTorch · Hugging Face · scikit-learn · LangChain · JAX ·
Qiskit · DisCoPy · pytket

**Cloud & CI** · AWS (EC2/VPC, SDK, CDK, CloudWatch) · Docker · Linux · GitHub Actions ·
Jenkins

<img width="100%" height="4" alt="" src="https://capsule-render.vercel.app/api?type=rect&color=0:1C1B18,50:1E4B7A,100:A6431E&height=4">

<div align="center">

### 📬 Get in touch

I'm looking for **Summer 2027 internships and new-grad software engineering roles**, and
I'll relocate anywhere in the US. Email is the fastest way to reach me.

<p>
  <a href="mailto:ivanwang8989@gmail.com"><img alt="Email Ivan" src="https://img.shields.io/badge/Email_me-ivanwang8989@gmail.com-1E4B7A?style=for-the-badge&logo=maildotru&logoColor=white"></a>
  <a href="https://iwang-1.github.io/"><img alt="Portfolio" src="https://img.shields.io/badge/See_the_work-Portfolio-A6431E?style=for-the-badge&logo=githubpages&logoColor=white"></a>
  <a href="https://www.linkedin.com/in/ivanwang1"><img alt="LinkedIn" src="https://img.shields.io/badge/Connect-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"></a>
</p>

<sub>Resume on request.</sub>

</div>
