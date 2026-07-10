# Hi, I'm Ivan Wang

Computer Science B.S./M.S. student at the University of Maryland, College Park — backend systems, ML/NLP, and research software. Seeking new-grad software engineering roles.

[LinkedIn](https://www.linkedin.com/in/ivanwang1)

## Currently

- Software Engineering Intern (Summer 2026), working on backend systems and cloud infrastructure
- Building an end-to-end astronomy star-catalog system in public — an ETL pipeline plus a REST API (below)
- Finishing my M.S. in Computer Science at UMD

## Featured work

### Star Catalog System — ETL pipeline + REST API

Two personal projects that form one end-to-end system, inspired by my open-source work on the UMD Observatory data archive:

```
observation CSVs ──▶ star-catalog-ingest ──▶ catalog.db (SQLite) ──▶ star-catalog-api ──▶ JSON
                     validate · clean · dedupe                       search · filter · stats
```

- **[star-catalog-ingest](https://github.com/iwang-1/star-catalog-ingest)** — ETL CLI that turns messy telescope observation CSVs into a validated, deduplicated SQLite catalog. Streaming validation with stable reject codes, idempotent hash-gated loads, ~95% test coverage, mypy `--strict`, CI on Python 3.11/3.12.
- **[star-catalog-api](https://github.com/iwang-1/star-catalog-api)** — typed FastAPI service over that catalog: name search, magnitude/constellation filters, a cone search that handles the RA 0/360 seam, pagination, and stats. Layered architecture, ~97% test coverage, Dockerized, CI green.

*Python · FastAPI · SQLite · pydantic · Docker · GitHub Actions*

### Open source — UMD Observatory CCD Data Archive

**[Four merged pull requests](https://github.com/warnerem/CCD-data-archive/pulls?q=is%3Apr+author%3Aiwang-1+is%3Amerged)** to the upstream repo, [warnerem/CCD-data-archive](https://github.com/warnerem/CCD-data-archive) — a Python / Flask / SQLite archive that makes years of UMD Observatory CCD astronomy data easier to access and search. Working with this data is what inspired the star-catalog projects above.

*Python · Flask · SQLite · JavaScript*

### Quantum NLP research (UMD FIRE)

**[FIRE-QML-WINNERS-QNLP](https://github.com/iwang-1/FIRE-QML-WINNERS-QNLP)** — a 3-person collaborative research project exploring quantum natural language processing for sentence classification. My contributions were the experiment datasets and project documentation.

*Python · DisCoPy · Qiskit · pytket*

## Skills

- **Languages:** Python (primary), Java, C/C++, SQL, JavaScript/TypeScript, Bash
- **Frameworks:** FastAPI, Flask, PyTorch, scikit-learn
- **Tools:** Git, Docker, Linux, SQLite/PostgreSQL, AWS, GitHub Actions CI, pytest

---

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=iwang-1&layout=compact&langs_count=6&hide=jupyter%20notebook,html,css" alt="Top languages" />
