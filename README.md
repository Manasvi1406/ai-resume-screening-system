# 🧠 AI Resume Screening System

An AI-assisted resume screening and candidate ranking system built using **Python, Natural Language Processing (NLP), Machine Learning techniques, and Streamlit**.

The application analyzes candidate resumes against a job description, extracts relevant skills, calculates text similarity using **TF-IDF and cosine similarity**, and generates a ranked list of candidates through an interactive web dashboard.

---

## ✨ Features

- 📄 Upload job descriptions
- 👤 Upload multiple candidate resumes
- 📑 Support for PDF, DOCX, and TXT resume files
- 🔍 Automatic resume text extraction
- 🧩 Skill extraction and matching
- 📊 TF-IDF-based text similarity
- 📐 Cosine similarity calculation
- 🎯 Combined candidate scoring
- 📈 Ranked candidate visualization
- 👀 Individual candidate analysis
- 📄 Original resume preview
- 🔎 Matched and missing skills
- 📥 CSV export of screening results
- 🌌 Dark neon/futuristic user interface
- 🧭 Separate Screening, Ranked Candidates, and Candidate Details pages
- 🧪 Sample job description and candidate resumes included

---

## 🖥️ Application Workflow

```text
Job Description
       ↓
Candidate Resumes
       ↓
Text Extraction
       ↓
Skill Extraction
       ↓
TF-IDF Vectorization
       ↓
Cosine Similarity
       ↓
Skill Match Score
       ↓
Candidate Ranking
```

---

## 🧠 How It Works

### 1. Resume Text Extraction

The system accepts candidate resumes in different file formats:

- PDF
- DOCX
- TXT

The uploaded resume content is extracted and converted into text for further processing.

### 2. Skill Extraction

The application contains a skills taxonomy containing technical and professional skills.

The system identifies skills appearing in:

- Job descriptions
- Candidate resumes

It then calculates the candidate's skill match and identifies:

- Matched Skills
- Missing Skills

### 3. TF-IDF Text Representation

The job description and candidate resumes are converted into numerical representations using **TF-IDF (Term Frequency-Inverse Document Frequency)**.

TF-IDF helps identify the importance of words within the job description and candidate resumes.

### 4. Cosine Similarity

Cosine similarity is used to compare the job description with each candidate resume.

A higher similarity indicates greater textual overlap between the candidate's resume and the job description.

### 5. Candidate Ranking

The system combines:

- Text similarity
- Skill matching

to generate an overall candidate score.

Candidates are then sorted according to their calculated scores.

---

## 📊 Candidate Analysis

For each candidate, the application provides information such as:

| Metric | Description |
|---|---|
| Final Score | Overall screening score |
| Text Similarity | Similarity between the job description and resume |
| Skill Match | Percentage of identified relevant skills |
| Matched Skills | Relevant skills found in the candidate resume |
| Missing Skills | Relevant skills not found in the candidate resume |

Users can inspect individual candidates through the **Candidate Details** page.

---

## 🖥️ Application Pages

### 💠 Screening

The main screening page provides separate sections for:

- Job Description
- Candidate Resumes
- Skill Configuration
- Screening Controls

Users can upload the required files and start the screening process.

### 📈 Ranked Candidates

Displays candidates according to their calculated screening scores.

The page provides an overview of:

- Candidate ranking
- Final score
- Text similarity
- Skill match

### 👤 Candidate Details

Provides detailed information about an individual candidate, including:

- Candidate name
- Final score
- Text similarity
- Skill match
- Matched skills
- Missing skills
- Resume preview

---

## 📂 Project Structure

```text
ai-resume-screening-system/
│
├── app.py
│
├── resume_screener/
│   ├── __init__.py
│   ├── extractor.py
│   ├── ranker.py
│   └── skills.py
│
├── sample_data/
│   ├── job_description.txt
│   └── resumes/
│       ├── Aisha Khan.txt
│       ├── Emily Chen.txt
│       └── Rohan Verma.txt
│
├── .streamlit/
│   └── config.toml
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web application |
| Scikit-learn | TF-IDF and cosine similarity |
| Pandas | Data processing |
| NumPy | Numerical operations |
| PyPDF | PDF text extraction |
| docx2txt | DOCX text extraction |
| HTML/CSS | UI customization |
| Git | Version control |
| GitHub | Source code hosting |

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Manasvi1406/ai-resume-screening-system.git
```

### 2. Open the Project Directory

```bash
cd ai-resume-screening-system
```

### 3. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

#### Linux / WSL / macOS

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will normally be available at:

```text
http://localhost:8501
```

Open the address in your web browser.

---

## 🧪 Try the Sample Data

Sample files are included in the repository.

### Job Description

```text
sample_data/job_description.txt
```

### Sample Resumes

```text
sample_data/resumes/Aisha Khan.txt
sample_data/resumes/Emily Chen.txt
sample_data/resumes/Rohan Verma.txt
```

You can use these files to test the screening system without creating your own data first.

---

## ⚙️ Customization

The system can be customized through the main project modules.

### `skills.py`

Used for managing the skills taxonomy and skill matching.

### `ranker.py`

Contains the candidate ranking and similarity calculation logic.

### `extractor.py`

Handles text extraction from supported resume formats.

### `app.py`

Contains the Streamlit application interface and application workflow.

---

## 🎯 Project Objectives

The project demonstrates the practical application of:

- Natural Language Processing
- TF-IDF text representation
- Cosine similarity
- Skill extraction
- Text processing
- Information extraction
- Data processing
- Candidate ranking
- Python application development
- Interactive dashboard development

---

## 🔮 Future Improvements

Possible future enhancements include:

- Transformer-based text embeddings
- Advanced NLP techniques
- Additional resume file formats
- Database integration
- User authentication
- Cloud deployment
- Advanced analytics dashboard
- Configurable scoring weights
- Screening history
- Improved contextual skill matching
- Automated candidate communication

---

## ⚠️ Limitations

This project is designed as an **AI-assisted resume screening and portfolio application**.

Candidate ranking is based primarily on textual similarity and identified skills. Therefore, the generated ranking should be treated as a screening aid rather than the sole basis for employment decisions.

---

## 👨‍💻 Author

**Manasvi Sharma**

B.Tech — Robotics & Automation

### Areas of Interest

- Artificial Intelligence
- Machine Learning
- Data Science
- Python
- Software Development
- Robotics & Automation

---

## 🔗 GitHub

Repository:

https://github.com/Manasvi1406/ai-resume-screening-system

---

## 📄 License

This project is released under the **MIT License**.
