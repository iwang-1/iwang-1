<div align="center">

<img width="100%" alt="Ivan Wang — distributed systems · storage engines · backend infrastructure" src="https://capsule-render.vercel.app/api?type=waving&color=0:102A43,50:1D4ED8,100:38BDF8&height=210&section=header&text=Ivan%20Wang&fontSize=62&fontColor=ffffff&animation=fadeIn&fontAlignY=36&desc=distributed%20systems%20%C2%B7%20storage%20engines%20%C2%B7%20backend%20infrastructure&descSize=18&descAlignY=57">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://readme-typing-svg.demolab.com/?font=Fira+Code&weight=600&size=20&pause=1000&color=38BDF8&center=true&vCenter=true&width=680&height=44&lines=Hi%2C+I'm+Ivan+%F0%9F%91%8B;AWS+SDE+Intern+(Summer+2026)+%E2%80%94+backend+%2B+cloud+infra;CS+B.S.%2FM.S.+%40+UMD+College+Park;I+build+systems+that+stay+correct+when+parts+fail;Seeking+new-grad+SWE+roles;Climbing+when+I'm+not+compiling">
  <img alt="Hi, I'm Ivan — AWS SDE Intern (Summer 2026) — CS B.S./M.S. @ UMD — seeking new-grad SWE roles" src="https://readme-typing-svg.demolab.com/?font=Fira+Code&weight=600&size=20&pause=1000&color=1D4ED8&center=true&vCenter=true&width=680&height=44&lines=Hi%2C+I'm+Ivan+%F0%9F%91%8B;AWS+SDE+Intern+(Summer+2026)+%E2%80%94+backend+%2B+cloud+infra;CS+B.S.%2FM.S.+%40+UMD+College+Park;I+build+systems+that+stay+correct+when+parts+fail;Seeking+new-grad+SWE+roles;Climbing+when+I'm+not+compiling">
</picture>

<p>
  <img alt="AWS SDE Intern, Summer 2026" src="https://custom-icon-badges.demolab.com/badge/AWS-SDE_Intern_(Summer_2026)-FF9900?style=for-the-badge&logo=aws&logoColor=white">
  <img alt="UMD Computer Science B.S./M.S., May 2027" src="https://img.shields.io/badge/UMD-CS_B.S.%2FM.S._%C2%B7_May_2027-102A43?style=for-the-badge">
  <img alt="Seeking new-grad SWE roles, 2027" src="https://img.shields.io/badge/New_Grad-SWE_%C2%B7_2027-16a34a?style=for-the-badge">
</p>
<p>
  <a href="https://iwang-1.github.io/"><img alt="Portfolio: iwang-1.github.io" src="https://img.shields.io/badge/Portfolio-iwang--1.github.io-8B5CF6?style=for-the-badge&logo=githubpages&logoColor=white"></a>
  <a href="https://www.linkedin.com/in/ivanwang1"><img alt="LinkedIn: ivanwang1" src="https://custom-icon-badges.demolab.com/badge/LinkedIn-ivanwang1-0A66C2?style=for-the-badge&logo=linkedin-white&logoColor=white"></a>
  <a href="mailto:ivanwang8989@gmail.com"><img alt="Email: ivanwang8989@gmail.com" src="https://img.shields.io/badge/Email-ivanwang8989@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white"></a>
</p>

</div>

## 👨‍💻 About

<table>
<tr>
<td width="55%" valign="top">
<h3>The short version</h3>
<ul>
  <li>☁️ <b>SDE Intern @ AWS (Summer 2026)</b> — EC2 Networking, backend systems &amp; cloud infrastructure</li>
  <li>🎓 <b>CS B.S./M.S.</b> — University of Maryland, College Park; Departmental Honors research track, finishing the M.S.</li>
  <li>🛠️ I build <b>across the stack</b> — backend services, systems software, and ML/NLP — and pick up new stacks fast</li>
  <li>🔬 I care about software you can <b>check</b>: tests, reproducible measurements, and honest limitations</li>
  <li>🎯 <b>Seeking new-grad software engineering roles</b> for 2027</li>
</ul>
</td>
<td width="45%" valign="top">
<h3>Currently</h3>
<p>
  <img alt="Full-stack software engineer" src="https://img.shields.io/badge/software_engineer-backend_%C2%B7_systems_%C2%B7_ML%2FNLP-1D4ED8?style=for-the-badge">
</p>
<table>
<tr><td>🧭</td><td><b>Building</b></td><td>systems, services, and ML/NLP in Go, Rust &amp; Python</td></tr>
<tr><td>☁️</td><td><b>Interning</b></td><td>backend + cloud infra @ AWS</td></tr>
<tr><td>🔬</td><td><b>Studying</b></td><td>M.S. CS @ UMD (research track)</td></tr>
<tr><td>🎯</td><td><b>Seeking</b></td><td>new-grad SWE roles for 2027</td></tr>
</table>
<p>
  <img alt="Upstream PRs: 4 merged, 1 open" src="https://img.shields.io/badge/upstream_PRs-4_merged_%C2%B7_1_open-2ea043?style=flat-square&logo=git&logoColor=white">
  <img alt="Public repos: systems, ML/NLP, tooling" src="https://img.shields.io/badge/public_repos-systems_%2B_ML%2FNLP-38BDF8?style=flat-square&logo=github&logoColor=white">
</p>
<sub>the research + open-source story lives on the <a href="https://iwang-1.github.io/projects/">portfolio</a> ↗</sub>
</td>
</tr>
</table>

<img width="100%" height="4" alt="" src="https://capsule-render.vercel.app/api?type=rect&color=0:102A43,50:1D4ED8,100:38BDF8&height=4">

## 🚀 Featured builds

Three systems built from scratch, each with a test harness designed before the thing it judges.

<table>
<tr>
<td width="50%" valign="top">
<h3>🧭 <a href="https://github.com/iwang-1/parallax-kv">parallax-kv</a></h3>
<p><b>Linearizable distributed key-value store in Go</b></p>
<p>Raft consensus from scratch: PreVote, ReadIndex linearizable reads, persist-before-send ordering, snapshots, a durable WAL, and a gRPC runtime.</p>
<p><sub>🔬 A deterministic harness replayed partitions, crashes, message loss, and delays across <b>2.9M client operations</b> — <b>zero</b> safety or linearizability violations, and it caught a precision bug in the checker itself.</sub></p>
<p>
  <img alt="Go" src="https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white">
  <img alt="Raft" src="https://img.shields.io/badge/Raft-0E7490?style=flat-square">
  <img alt="gRPC" src="https://img.shields.io/badge/gRPC-244C5A?style=flat-square&logo=google&logoColor=white">
  <img alt="Porcupine" src="https://img.shields.io/badge/Porcupine-A855F7?style=flat-square">
</p>
<a href="https://github.com/iwang-1/parallax-kv"><b>Inspect the repo →</b></a>
</td>
<td width="50%" valign="top">
<h3>💾 <a href="https://github.com/iwang-1/accretion-db">accretion-db</a></h3>
<p><b>Crash-safe LSM storage engine in Rust</b></p>
<p>CRC-framed write-ahead log with group commit, memtables, block-based SSTables, bloom filters, and size-tiered compaction — with <code>unsafe</code> forbidden.</p>
<p><sub>💥 A fault-injection harness simulates power loss at every write and fsync boundary: <b>zero acknowledged-write loss</b> across the crash sweep, with a <b>~29x</b> WAL-bound edge from group commit.</sub></p>
<p>
  <img alt="Rust" src="https://img.shields.io/badge/Rust-CE422B?style=flat-square&logo=rust&logoColor=white">
  <img alt="LSM tree" src="https://img.shields.io/badge/LSM_tree-0E7490?style=flat-square">
  <img alt="group commit" src="https://img.shields.io/badge/group_commit-244C5A?style=flat-square">
  <img alt="proptest" src="https://img.shields.io/badge/proptest-A855F7?style=flat-square">
</p>
<a href="https://github.com/iwang-1/accretion-db"><b>Inspect the repo →</b></a>
</td>
</tr>
<tr></tr>
<tr>
<td width="50%" valign="top">
<h3>🧲 <a href="https://github.com/iwang-1/lodestone">lodestone</a></h3>
<p><b>SIMD-accelerated vector search engine in Rust</b></p>
<p>An HNSW proximity graph and an IVF-PQ compressed index over hand-written AVX-512 distance kernels — for embeddings and RAG retrieval.</p>
<p><sub>📈 On 50,000 128-d vectors, single core: HNSW hits <b>0.976 recall@10 at ~31,800 QPS</b> — a <b>30–48x</b> speedup over the exact scan at 90%+ recall; IVF-PQ holds <b>0.975 recall@10 at 16x</b> compression.</sub></p>
<p>
  <img alt="Rust" src="https://img.shields.io/badge/Rust-CE422B?style=flat-square&logo=rust&logoColor=white">
  <img alt="HNSW" src="https://img.shields.io/badge/HNSW-0E7490?style=flat-square">
  <img alt="IVF-PQ" src="https://img.shields.io/badge/IVF--PQ-244C5A?style=flat-square">
  <img alt="AVX-512" src="https://img.shields.io/badge/AVX--512_SIMD-A855F7?style=flat-square">
</p>
<a href="https://github.com/iwang-1/lodestone"><b>Inspect the repo →</b></a>
</td>
<td width="50%" valign="top">
<h3>🌍 Research &amp; open source</h3>
<p>
  <img alt="4 merged PRs" src="https://img.shields.io/badge/MERGED-%C3%974-2ea043?style=flat-square&logo=git&logoColor=white"> <a href="https://github.com/warnerem/CCD-data-archive/pulls?q=is%3Apr+author%3Aiwang-1+is%3Amerged"><b>CCD-data-archive</b></a><br>
  Four merged PRs to the UMD Observatory astronomy archive — Python/Flask/SQLite, 50,000+ records.
</p>
<p>
  <img alt="open, not merged" src="https://img.shields.io/badge/OPEN-under_review-d29922?style=flat-square"> <a href="https://github.com/Quantinuum/lambeq/pull/259"><b>lambeq #259</b></a><br>
  One open upstream PR adding a <code>LAMBEQ_MODELS_URL</code> override.
</p>
<p>
  <img alt="research artifact" src="https://img.shields.io/badge/research-A855F7?style=flat-square"> <a href="https://github.com/iwang-1/FIRE-QML-WINNERS-QNLP"><b>Quantum NLP (FIRE)</b></a><br>
  Four-person research artifact — DisCoPy, Qiskit, pytket, JAX. My slice: dataset prep, integration, and docs.
</p>
</td>
</tr>
</table>

<img width="100%" height="4" alt="" src="https://capsule-render.vercel.app/api?type=rect&color=0:38BDF8,50:1D4ED8,100:102A43&height=4">

## 🧰 Toolbox

**Languages**

![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-CE422B?style=flat-square&logo=rust&logoColor=white)
![Java](https://img.shields.io/badge/Java-E76F00?style=flat-square&logo=openjdk&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![C](https://img.shields.io/badge/C-283593?style=flat-square&logo=c&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white)

**Backend & systems**

![gRPC](https://img.shields.io/badge/gRPC-244C5A?style=flat-square&logo=google&logoColor=white)
![Protobuf](https://img.shields.io/badge/Protobuf-0E7490?style=flat-square)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)

**ML & research**

![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![Qiskit](https://img.shields.io/badge/Qiskit-6929C4?style=flat-square&logo=qiskit&logoColor=white)

**Infrastructure**

![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)

<sub>…plus JUnit 5, and CDK/CloudWatch on the job.</sub>

<img width="100%" height="4" alt="" src="https://capsule-render.vercel.app/api?type=rect&color=0:102A43,50:1D4ED8,100:38BDF8&height=4">

<div align="center">

<p>
  <a href="https://iwang-1.github.io/"><b>Portfolio</b></a> ·
  <a href="https://www.linkedin.com/in/ivanwang1"><b>LinkedIn</b></a> ·
  <a href="mailto:ivanwang8989@gmail.com"><b>Email</b></a>
</p>

<sub>Thanks for stopping by.</sub>

<img width="100%" alt="" src="https://capsule-render.vercel.app/api?type=waving&color=0:38BDF8,50:1D4ED8,100:102A43&height=110&section=footer">

</div>
