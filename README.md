# 🧠 AI-Powered Resume Screening System

An AI-powered Resume Screening System built with **Python**, **NLP**, and
**Machine Learning** that analyzes resumes, extracts key skills, ranks
candidates against a job description using **TF-IDF** and **cosine
similarity**, and presents everything through an interactive **Streamlit**
dashboard for automated candidate evaluation.

## ✨ Features

- 📄 **Multi-format resume parsing** — upload resumes as PDF, DOCX, or TXT
- 🧩 **Skill extraction** — NLP-based keyword matching against an editable
  skills taxonomy (programming languages, ML/DS tools, cloud, soft skills…)
- 📊 **TF-IDF + Cosine Similarity ranking** — resumes are vectorized against
  the job description text and scored by semantic overlap
- 🎯 **Blended scoring** — combine text similarity with explicit
  required-skill match percentage (adjustable weighting)
- 🖥️ **Interactive Streamlit dashboard** — upload, rank, inspect, and
  export results, all in the browser
- 📥 **CSV export** of the final ranking table
- 🧪 **Sample data included** — a sample job description and 3 sample
  resumes so you can try it immediately

## 🗂️ Project Structure

```
resume-screening-system/
├── app.py                     # Streamlit dashboard (entry point)
├── resume_screener/
│   ├── __init__.py
│   ├── extractor.py           # PDF/DOCX/TXT text extraction
│   ├── skills.py              # Skills taxonomy + extraction logic
│   └── ranker.py              # TF-IDF + cosine similarity ranking
├── sample_data/
│   ├── job_description.txt
│   └── resumes/
│       ├── Aisha Khan.txt
│       ├── Rohan Verma.txt
│       └── Emily Chen.txt
├── .streamlit/config.toml     # Streamlit theme config
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### 1. Clone and set up a virtual environment

```bash
git clone https://github.com/<your-username>/resume-screening-system.git
cd resume-screening-system

python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

The dashboard will open in your browser at `http://localhost:8501`.

### 4. Try it with the sample data

- Paste the contents of `sample_data/job_description.txt` into the
  **Job Description** box (or upload it as a file).
- Upload the three files from `sample_data/resumes/` as candidate resumes.
- Click **🔍 Rank Candidates** to see the ranked results.

## ⚙️ How It Works

1. **Text extraction** — `resume_screener/extractor.py` pulls raw text out
   of PDF (`pypdf`), DOCX (`docx2txt`), or TXT resumes.
2. **Skill extraction** — `resume_screener/skills.py` matches resume and JD
   text against a curated skills taxonomy using word-boundary regex
   matching (fast, transparent, and easy to extend).
3. **Ranking** — `resume_screener/ranker.py` builds a TF-IDF matrix over the
   job description + all resumes using `scikit-learn`'s `TfidfVectorizer`,
   computes cosine similarity between the JD and each resume, and blends
   that with the explicit skill-match percentage into a final score.
4. **Dashboard** — `app.py` wires it all together in Streamlit: file
   uploads, skill configuration, a ranked results table, a bar chart, a
   per-candidate detail view, and CSV export.

## 🛠️ Customizing

- **Add your own skills**: edit `SKILLS_DB` in `resume_screener/skills.py`.
- **Adjust scoring weight**: use the slider in the app, or change the
  default `skill_weight` in `rank_resumes()` in `resume_screener/ranker.py`.
- **Support more file types**: extend `extract_text()` in
  `resume_screener/extractor.py`.

## 📦 Tech Stack

Python · Streamlit · scikit-learn · pandas · pypdf · docx2txt

## 📄 License

MIT — free to use and modify.
