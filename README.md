# Hi, I'm Ivan Wang

Computer Science B.S./M.S. student at the University of Maryland, College Park — backend systems, ML/NLP, and research software. Seeking new-grad software engineering roles.

[LinkedIn](https://www.linkedin.com/in/ivanwang1) · [Personal site](https://iwang-1.github.io/)

## Currently

- Software Engineering Intern (Summer 2026), working on backend systems and cloud infrastructure
- Finishing my M.S. in Computer Science at UMD
- Away from the keyboard: building mechanical keyboards and PCs, and climbing

## Featured work

### Open source — UMD Observatory CCD Data Archive

**[Four merged pull requests](https://github.com/warnerem/CCD-data-archive/pulls?q=is%3Apr+author%3Aiwang-1+is%3Amerged)** to the upstream repo, [warnerem/CCD-data-archive](https://github.com/warnerem/CCD-data-archive) — a Python / Flask / SQLite archive that makes years of UMD Observatory CCD astronomy data easier to access and search.

*Python · Flask · SQLite · JavaScript*

### Cross-domain sentiment under domain shift — DistilBERT + DANN

**[cross-domain-sentiment-dann](https://github.com/iwang-1/cross-domain-sentiment-dann)** — domain generalization for sentiment classification across Yelp, Amazon, Twitter, and Reddit, evaluated leave-one-domain-out on a held-out platform the model never saw in training. A domain-adversarial network (gradient-reversal layer on a shared DistilBERT encoder) lifts held-out-domain accuracy from a near-random 50.8% baseline to 67.7% on average — 74.2% at best, on Yelp — on ~1,000-example-per-domain subsets. The README says plainly that an off-the-shelf SST-2 model still wins on the review domains and on average; the result is how much of the domain-shift gap adversarial training recovers under data scarcity, not a new state of the art. UMD CMSC472 team project.

*Python · PyTorch · Hugging Face Transformers · DistilBERT*

### Quantum NLP research (UMD FIRE)

**[FIRE-QML-WINNERS-QNLP](https://github.com/iwang-1/FIRE-QML-WINNERS-QNLP)** — a 3-person collaborative research project exploring quantum natural language processing for sentence classification. My contributions were dataset preparation and integration, and the project documentation.

Also: an **[open pull request to Quantinuum/lambeq](https://github.com/Quantinuum/lambeq/pull/259)**, the quantum NLP library — allow overriding the model download URL via `LAMBEQ_MODELS_URL` (open, not yet merged).

*Python · DisCoPy · Qiskit · pytket*

## Skills

- **Languages:** Python (primary), Java, C/C++, SQL, JavaScript/TypeScript, Bash
- **Frameworks:** FastAPI, Flask, React, PyTorch, scikit-learn
- **Tools:** Git, Docker, Linux, SQLite/PostgreSQL, AWS, GitHub Actions CI, pytest
