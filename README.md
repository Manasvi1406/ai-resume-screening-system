# 🧠 AI Resume Screening System

An AI-assisted resume screening and candidate ranking system built with **Python, Natural Language Processing (NLP), Machine Learning techniques, and Streamlit**.

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
                ┌──────────────────────┐
                │   Job Description    │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │  Candidate Resumes   │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │   Text Extraction    │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │   Skill Extraction   │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ TF-IDF Vectorization │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │  Cosine Similarity   │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │  Skill Match Score   │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │  Candidate Ranking   │
                └──────────────────────┘

🧠 How It Works
1. Resume Text Extraction
The system extracts text from uploaded resumes using dedicated extraction modules.
Supported formats include:
- PDF
- DOCX
- TXT
The extracted content is passed to the screening pipeline for further processing.
2. Skill Extraction
The application maintains a skills taxonomy containing technical and professional skills.
The system identifies skills appearing in:
- Job descriptions
- Candidate resumes
It then calculates the candidate's skill match and identifies:
- Matched Skills
- Missing Skills
3. TF-IDF Text Representation
The job description and candidate resumes are converted into numerical representations using TF-IDF (Term Frequency–Inverse Document Frequency).
TF-IDF helps identify the importance of words within the job description and candidate resumes.
4. Cosine Similarity
Cosine similarity is used to compare the job description with each candidate resume.
A higher similarity indicates greater textual overlap between the candidate's resume and the job description.
5. Candidate Ranking
The system combines text similarity information with skill matching to generate a final candidate score.
Candidates are then sorted according to their calculated scores.
📊 Candidate Analysis
For each candidate, the application provides information such as:
Metric	Description
Final Score	Overall screening score
Text Similarity	Similarity between the job description and resume
Skill Match	Percentage of identified relevant skills
Matched Skills	Relevant skills found in the candidate resume
Missing Skills	Relevant skills not found in the candidate resume


Users can inspect individual candidates through the Candidate Details page.
🖥️ Application Pages
🔹 Screening
The main screening page provides separate sections for:
- Job Description
- Candidate Resumes
- Skill Configuration
- Candidate Ranking
Users can upload the required files and configure the screening criteria before starting the ranking process.
🔹 Ranked Candidates
The Ranked Candidates page displays the screening results.
It provides:
- Candidate ranking
- Final scores
- Text similarity
- Skill match
- Score visualization
- CSV export
🔹 Candidate Details
The Candidate Details page provides a detailed analysis of an individual candidate.
It includes:
- Final score
- Text similarity
- Skill match
- Matched skills
- Missing skills
- Original uploaded resume preview
- Extracted resume information
📂 Project Structure
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

🛠️ Technology Stack
Technology	Purpose
Python	Core programming language
Streamlit	Interactive web application
Scikit-learn	TF-IDF and cosine similarity
Pandas	Data processing and result handling
NumPy	Numerical operations
PyPDF	PDF text extraction
docx2txt	DOCX text extraction
HTML/CSS	User interface customization
Git	Version control
GitHub	Source code hosting


🚀 Installation
1. Clone the repository
git clone https://github.com/Manasvi1406/ai-resume-screening-system.git

2. Navigate to the project
cd ai-resume-screening-system

3. Create a virtual environment
python -m venv venv

4. Activate the virtual environment
Windows
venv\Scripts\activate

Linux / WSL / macOS
source venv/bin/activate

5. Install dependencies
pip install -r requirements.txt

▶️ Run the Application
Start the Streamlit application:
streamlit run app.py

The application will normally be available at:
http://localhost:8501

Open the address in your browser.
🧪 Try the Sample Data
The repository contains sample data that can be used to test the application.
Job Description
sample_data/job_description.txt

Sample Resumes
sample_data/resumes/
├── Aisha Khan.txt
├── Emily Chen.txt
└── Rohan Verma.txt

Basic Workflow
1. Start the application.
2. Upload or enter the job description.
3. Upload the candidate resumes.
4. Configure the required skills.
5. Run the candidate ranking.
6. Open Ranked Candidates.
7. Select a candidate to view detailed results.
8. Export the ranking as CSV if required.
⚙️ Customization
Add or Modify Skills
The skills taxonomy can be modified in:
resume_screener/skills.py

Modify Ranking Logic
The candidate ranking logic is implemented in:
resume_screener/ranker.py

Modify Resume Extraction
Resume file processing is handled in:
resume_screener/extractor.py

Customize the Interface
The Streamlit application and visual styling are primarily handled in:
app.py

🎯 Project Objectives
This project demonstrates the practical application of:
- Natural Language Processing
- TF-IDF vectorization
- Cosine similarity
- Skill extraction
- Text processing
- Information extraction
- Data processing
- Candidate ranking
- Interactive dashboard development
- Python application development
🔮 Future Improvements
Potential future improvements include:
- 🤗 Transformer-based semantic embeddings
- 🧠 Advanced NLP models
- 📄 Additional resume formats
- 🗃️ Candidate database integration
- 🔐 User authentication
- ☁️ Cloud deployment
- 📊 Advanced recruitment analytics
- 📧 Automated candidate communication
- ⚖️ Configurable scoring weights
- 📈 Candidate history and analytics
- 🔎 More advanced contextual skill matching
⚠️ Limitations
This project is designed as a resume screening assistance and portfolio demonstration system.
The candidate ranking is based primarily on textual similarity and identified skills. Therefore, the generated ranking should be treated as a screening aid rather than the sole basis for employment decisions.
📌 Sample Project Output
The application generates a candidate ranking containing information such as:
Candidate
Final Score
Text Similarity
Skill Match
Matched Skills
Missing Skills

Users can also inspect individual candidates and view their uploaded resumes through the Candidate Details page.
👨‍💻 Author
Manasvi Sharma
B.Tech — Robotics & Automation
Areas of Interest
- Artificial Intelligence
- Machine Learning
- Data Science
- Python
- Software Development
- Robotics & Automation
🔗 GitHub Repository
AI Resume Screening System
https://github.com/Manasvi1406/ai-resume-screening-system
📄 License
This project is available under the MIT License.
