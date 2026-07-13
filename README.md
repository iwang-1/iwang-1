# Hi, I'm Ivan Wang

Computer Science B.S./M.S. student at the University of Maryland, College Park — backend systems, ML/NLP, and research software. Seeking new-grad software engineering roles.

[LinkedIn](https://www.linkedin.com/in/ivanwang1) · [Personal site](https://iwang-1.github.io/)

## Currently

- Software Engineering Intern (Summer 2026), working on backend systems and cloud infrastructure
- Building an end-to-end astronomy star-catalog system — an ETL pipeline, a REST API, an interactive sky map, and an ML spectral classifier (below)
- Finishing my M.S. in Computer Science at UMD

## Featured work

### Star Catalog System — ETL pipeline + REST API + sky map + ML classifier

Three personal projects that form one end-to-end system, plus an ML companion trained on its data — inspired by my open-source work on the UMD Observatory data archive:

```
observation CSVs ──▶ star-catalog-ingest ──▶ catalog.db (SQLite) ──▶ star-catalog-api ──▶ star-catalog-web
                     validate · clean · dedupe                       search · filter · stats  sky map · search UI

star-catalog-web ──▶ stars.json (HYG snapshot) ──▶ star-spectral-classifier (OBAFGKM from B–V)
```

- **[star-catalog-ingest](https://github.com/iwang-1/star-catalog-ingest)** — ETL CLI that turns messy telescope observation CSVs into a validated, deduplicated SQLite catalog. Streaming validation with stable reject codes, idempotent hash-gated loads, ~95% test coverage, mypy `--strict`, CI on Python 3.11–3.14.
- **[star-catalog-api](https://github.com/iwang-1/star-catalog-api)** — typed FastAPI service over that catalog: name search, magnitude and catalog-designation-prefix filters, a cone search that handles the RA 0/360 seam, pagination, and stats. Layered architecture, ~97% test coverage, Dockerized, CI on Python 3.11/3.12.
- **[star-catalog-web](https://github.com/iwang-1/star-catalog-web)** — interactive sky map and searchable catalog of 8,920 naked-eye HYG stars (React + TypeScript + Vite): magnitude-scaled, color-indexed star markers, linked map/table selection, and live search. Verified end-to-end in headless Chromium with Playwright. **[Live demo](https://iwang-1.github.io/star-catalog-web/)**
- **[star-spectral-classifier](https://github.com/iwang-1/star-spectral-classifier)** — ML companion that predicts OBAFGKM spectral class from B–V color on the sky map's HYG snapshot. Built to beat a 72% textbook-physics baseline honestly — 79.5% accuracy / 0.665 macro-F1 on a seeded stratified hold-out, a per-class error analysis that owns the O class it never gets right, mypy `--strict`, CI on Python 3.11–3.13.

<a href="https://iwang-1.github.io/star-catalog-web/"><img src="https://raw.githubusercontent.com/iwang-1/star-catalog-web/main/docs/screenshot.png" alt="star-catalog-web — sky map and searchable catalog table (click for the live demo)" width="800" /></a>

*Python · FastAPI · SQLite · pydantic · scikit-learn · TypeScript · React · Docker · GitHub Actions*

### Open source — UMD Observatory CCD Data Archive

**[Four merged pull requests](https://github.com/warnerem/CCD-data-archive/pulls?q=is%3Apr+author%3Aiwang-1+is%3Amerged)** to the upstream repo, [warnerem/CCD-data-archive](https://github.com/warnerem/CCD-data-archive) — a Python / Flask / SQLite archive that makes years of UMD Observatory CCD astronomy data easier to access and search. Working with this data is what inspired the star-catalog projects above.

*Python · Flask · SQLite · JavaScript*

### Cross-domain sentiment under domain shift — DistilBERT + DANN

**[cross-domain-sentiment-dann](https://github.com/iwang-1/cross-domain-sentiment-dann)** — domain generalization for sentiment classification across Yelp, Amazon, Twitter, and Reddit, evaluated leave-one-domain-out on a held-out platform the model never saw in training. A domain-adversarial network (gradient-reversal layer on a shared DistilBERT encoder) lifts held-out-domain accuracy from a near-random 50.8% baseline to 67.7% on average — 74.2% at best, on Yelp — on ~1,000-example-per-domain subsets. The README says plainly that an off-the-shelf SST-2 model still wins outright; the result is how much of the domain-shift gap adversarial training recovers under data scarcity, not a new state of the art. UMD CMSC472 team project.

*Python · PyTorch · Hugging Face Transformers · DistilBERT*

### Quantum NLP research (UMD FIRE)

**[FIRE-QML-WINNERS-QNLP](https://github.com/iwang-1/FIRE-QML-WINNERS-QNLP)** — a 3-person collaborative research project exploring quantum natural language processing for sentence classification. My contributions were dataset preparation and integration, and the project documentation.

Also: an **[open pull request to Quantinuum/lambeq](https://github.com/Quantinuum/lambeq/pull/259)**, the quantum NLP library — allow overriding the model download URL via `LAMBEQ_MODELS_URL` (open, not yet merged).

*Python · DisCoPy · Qiskit · pytket*

## Skills

- **Languages:** Python (primary), Java, C/C++, SQL, JavaScript/TypeScript, Bash
- **Frameworks:** FastAPI, Flask, React, PyTorch, scikit-learn
- **Tools:** Git, Docker, Linux, SQLite/PostgreSQL, AWS, GitHub Actions CI, pytest
