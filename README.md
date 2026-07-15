<div align="center">

<img width="100%" alt="Ivan Wang - distributed systems, backend engineering, and ML/NLP" src="https://capsule-render.vercel.app/api?type=waving&color=0:0C2438,55:0891B2,100:22D3EE&height=215&section=header&text=Ivan%20Wang&fontSize=62&fontColor=F4F8F9&animation=fadeIn&fontAlignY=36&desc=systems%20that%20stay%20correct%20when%20parts%20fail&descSize=18&descAlignY=57">

**Distributed systems &middot; storage engines &middot; backend infrastructure &middot; ML/NLP**

<p>
  <img alt="AWS SDE Intern, Summer 2026" src="https://img.shields.io/badge/AWS-SDE_Intern_%C2%B7_Summer_2026-FF9900?style=for-the-badge&logo=amazonwebservices&logoColor=111827">
  <img alt="UMD Computer Science BS/MS, May 2027" src="https://img.shields.io/badge/UMD-CS_B.S.%2FM.S._%C2%B7_May_2027-0C2438?style=for-the-badge">
  <img alt="Seeking new graduate software engineering roles" src="https://img.shields.io/badge/New_Grad-SWE_%C2%B7_2027-0891B2?style=for-the-badge">
</p>
<p>
  <a href="https://iwang-1.github.io/"><img alt="Portfolio" src="https://img.shields.io/badge/Portfolio-iwang--1.github.io-0891B2?style=for-the-badge&logo=githubpages&logoColor=white"></a>
  <a href="https://www.linkedin.com/in/ivanwang1"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-ivanwang1-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"></a>
  <a href="mailto:ivanwang8989@gmail.com"><img alt="Email Ivan Wang" src="https://img.shields.io/badge/Email-ivanwang8989%40gmail.com-0E7490?style=for-the-badge&logo=gmail&logoColor=white"></a>
</p>

</div>

## About

I'm a software engineer focused on **distributed systems, storage, and backend infrastructure**. I like software whose correctness can be tested under crashes, partitions, delayed messages, and hostile schedules, not just on the happy path.

- **SDE Intern at AWS (Summer 2026):** backend systems and cloud infrastructure
- **B.S./M.S. in Computer Science at UMD:** Departmental Honors research track, graduating May 2027
- **Open source:** four merged pull requests in the UMD Observatory archive and one upstream lambeq PR under review
- **Seeking:** new-grad software engineering roles starting Summer 2027

## Featured Systems

<table>
<tr>
<td width="50%" valign="top">
<h3><a href="https://github.com/iwang-1/parallax-kv">parallax-kv</a></h3>
<p><b>Three-node Raft key-value store in Go</b></p>
<p>PreVote, ReadIndex, persist-before-send ordering, snapshots, a durable WAL, gRPC, and deterministic fault simulation.</p>
<p><b>1,400 fault scenarios</b> and <b>2,914,245 client operations</b> with zero safety or linearizability violations.</p>
<p>
  <img alt="Go" src="https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white">
  <img alt="Raft" src="https://img.shields.io/badge/Raft-0E7490?style=flat-square">
  <img alt="gRPC" src="https://img.shields.io/badge/gRPC-244C5A?style=flat-square&logo=google&logoColor=white">
</p>
</td>
<td width="50%" valign="top">
<h3><a href="https://github.com/iwang-1/accretion-db">accretion-db</a></h3>
<p><b>Crash-tested LSM-tree engine in safe Rust</b></p>
<p>CRC-framed WAL, group commit, memtables, block SSTables, bloom filters, compaction, and a fault-injecting storage layer.</p>
<p><b>2,640 crash executions</b> with zero acknowledged-write loss; about <b>29x WAL-bound</b> group-commit throughput.</p>
<p>
  <img alt="Rust" src="https://img.shields.io/badge/Rust-111827?style=flat-square&logo=rust&logoColor=white">
  <img alt="LSM tree" src="https://img.shields.io/badge/LSM_tree-0891B2?style=flat-square">
  <img alt="Property testing" src="https://img.shields.io/badge/property_testing-0E7490?style=flat-square">
</p>
</td>
</tr>
</table>

## Shipped And Researched

| Project | What it demonstrates |
| --- | --- |
| [UMD Observatory CCD Data Archive](https://github.com/warnerem/CCD-data-archive) | Python/Flask/SQLite archive serving 50,000+ records; four pull requests merged upstream and pipeline runtime reduced 75% |
| [Cross-Domain Sentiment DANN](https://github.com/iwang-1/cross-domain-sentiment-dann) | DistilBERT domain-adversarial training across Yelp, Amazon, Twitter, and Reddit, with explicit baselines and limitations |
| [FIRE QML WINNERS QNLP](https://github.com/iwang-1/FIRE-QML-WINNERS-QNLP) | Four-person quantum NLP research artifact; I owned dataset preparation, workflow integration, and documentation |
| [This Portfolio](https://github.com/iwang-1/iwang-1.github.io) | React/TypeScript multi-page site with static prerendering, no-JS fallbacks, factual guardrails, and Playwright verification |

## Upstream Work

- **Merged x4:** [CCD-data-archive pull requests](https://github.com/warnerem/CCD-data-archive/pulls?q=is%3Apr+author%3Aiwang-1+is%3Amerged)
- **Under review:** [lambeq #259](https://github.com/Quantinuum/lambeq/pull/259), adding a configurable model-download base URL

## Toolbox

<div align="center">

<picture>
  <source media="(prefers-color-scheme: light)" srcset="https://skillicons.dev/icons?i=go,rust,py,java,ts,js,bash,react,pytorch,sklearn,aws,docker,linux,git,postgres,sqlite,githubactions&perline=9&theme=light">
  <img alt="Go, Rust, Python, Java, TypeScript, JavaScript, Bash, React, PyTorch, scikit-learn, AWS, Docker, Linux, Git, PostgreSQL, SQLite, and GitHub Actions" src="https://skillicons.dev/icons?i=go,rust,py,java,ts,js,bash,react,pytorch,sklearn,aws,docker,linux,git,postgres,sqlite,githubactions&perline=9&theme=dark">
</picture>

<sub>Also: Raft, gRPC/Protobuf, LSM trees, Flask/FastAPI, JUnit 5, Hugging Face, SQL, and Playwright.</sub>

</div>

## Beyond The Terminal

I'm Secretary of the **UMD Climbing Club**, where I organize eight trips a semester and helped grow attendance 30%. I also build mechanical keyboards and custom PCs, usually with more attention to the internals than the cable management deserves.

<div align="center">

<a href="https://iwang-1.github.io/"><b>Portfolio</b></a> &middot;
<a href="https://www.linkedin.com/in/ivanwang1"><b>LinkedIn</b></a> &middot;
<a href="mailto:ivanwang8989@gmail.com"><b>Email</b></a>

<img width="100%" alt="" src="https://capsule-render.vercel.app/api?type=waving&color=0:22D3EE,45:0891B2,100:0C2438&height=105&section=footer">

</div>
