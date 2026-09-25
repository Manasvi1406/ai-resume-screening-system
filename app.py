"""AI-Powered Resume Screening System - neon multi-page Streamlit UI."""

import io

import pandas as pd
import streamlit as st

from resume_screener.extractor import extract_text
from resume_screener.ranker import rank_resumes
from resume_screener.skills import SKILLS_DB, extract_skills


st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="🧠",
    layout="wide",
)


st.markdown(
    """
<style>
.stApp {
    background:
      radial-gradient(circle at 12% 8%, rgba(124,58,237,.20), transparent 28%),
      radial-gradient(circle at 88% 10%, rgba(34,211,238,.12), transparent 25%),
      radial-gradient(circle at 55% 100%, rgba(217,70,239,.12), transparent 30%),
      #05040d;
    color:#f7f5ff;
}

[data-testid="stHeader"]{
    background:rgba(5,4,13,.75)
}

.block-container{
    max-width:1500px;
    padding-top:1.5rem;
    padding-bottom:4rem
}

h1{
    font-size:clamp(2.3rem,4vw,4rem)!important;
    letter-spacing:-.045em!important;
    background:linear-gradient(90deg,#fff,#d8b4fe 48%,#67e8f9);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    text-shadow:0 0 30px rgba(168,85,247,.22)
}

h2,h3{
    color:#f8f7ff!important;
    letter-spacing:-.02em
}

p,[data-testid="stCaptionContainer"]{
    color:#a8a2b9
}

/* top navigation */
.nav-title{
    font-size:.78rem;
    text-transform:uppercase;
    letter-spacing:.16em;
    color:#8b82a5;
    margin-bottom:.45rem
}

.nav-current{
    color:#fff;
    font-weight:700
}

.nav-hint{
    color:#78718e;
    font-size:.78rem;
    margin-top:.35rem
}

.stButton>button{
    border-radius:12px!important;
    border:1px solid rgba(167,139,250,.35)!important;
    background:rgba(15,10,30,.78)!important;
    color:#e9e4ff!important;
    font-weight:650!important;
    box-shadow:0 0 18px rgba(124,58,237,.08);
    transition:.2s
}

.stButton>button:hover{
    border-color:#67e8f9!important;
    box-shadow:
        0 0 25px rgba(103,232,249,.18),
        0 0 25px rgba(168,85,247,.18);
    transform:translateY(-1px)
}

.nav-active button{
    background:linear-gradient(
        90deg,
        #7c3aed,
        #9333ea 55%,
        #0891b2
    )!important;
    color:#fff!important;
    border-color:#a78bfa!important;
    box-shadow:0 0 26px rgba(124,58,237,.35)!important
}

/* cards */
.neon-card{
    background:
        linear-gradient(
            145deg,
            rgba(20,14,40,.92),
            rgba(8,7,20,.88)
        );
    border:1px solid rgba(167,139,250,.20);
    border-radius:22px;
    padding:1.35rem 1.45rem;
    box-shadow:
        inset 0 1px 0 rgba(255,255,255,.04),
        0 20px 65px rgba(0,0,0,.25);
    min-height:170px
}

.neon-card:hover{
    border-color:rgba(103,232,249,.35);
    box-shadow:
        0 0 30px rgba(124,58,237,.12),
        inset 0 1px 0 rgba(255,255,255,.05)
}

.card-icon{
    font-size:1.65rem;
    margin-bottom:.35rem
}

.card-title{
    font-size:1.25rem;
    font-weight:750;
    color:#fff
}

.card-copy{
    color:#9d96ae;
    line-height:1.55;
    font-size:.93rem
}

.card-status{
    display:inline-block;
    margin-top:.8rem;
    padding:.28rem .65rem;
    border:1px solid rgba(103,232,249,.25);
    border-radius:999px;
    color:#a5f3fc;
    background:rgba(34,211,238,.05);
    font-size:.75rem
}

.section-card{
    background:
        linear-gradient(
            145deg,
            rgba(17,12,34,.90),
            rgba(8,7,19,.86)
        );
    border:1px solid rgba(167,139,250,.18);
    border-radius:22px;
    padding:1rem 1.1rem;
    box-shadow:0 18px 55px rgba(0,0,0,.24)
}

.stTextArea textarea,
.stTextInput input,
[data-baseweb="select"]>div{
    background:rgba(8,6,19,.9)!important;
    color:#f7f5ff!important;
    border:1px solid rgba(139,92,246,.30)!important;
    border-radius:13px!important
}

.stTextArea textarea:focus,
.stTextInput input:focus{
    border-color:#a855f7!important;
    box-shadow:
        0 0 0 1px #a855f7,
        0 0 24px rgba(168,85,247,.22)!important
}

[data-testid="stFileUploader"]{
    background:rgba(8,6,19,.65);
    border:1px dashed rgba(103,232,249,.35);
    border-radius:17px;
    padding:.35rem
}

[data-testid="stFileUploader"] section{
    background:transparent!important
}

.stButton>button[kind="primary"]{
    background:
        linear-gradient(
            90deg,
            #7c3aed,
            #9333ea 50%,
            #06b6d4
        )!important;
    color:#fff!important;
    border-color:rgba(167,139,250,.55)!important;
    box-shadow:0 0 28px rgba(124,58,237,.32)
}

[data-testid="stMetric"]{
    background:
        linear-gradient(
            145deg,
            rgba(21,14,42,.96),
            rgba(9,7,22,.92)
        );
    border:1px solid rgba(168,85,247,.24);
    border-radius:18px;
    padding:1rem;
    box-shadow:0 0 25px rgba(124,58,237,.09)
}

[data-testid="stMetricLabel"]{
    color:#a5f3fc!important
}

[data-testid="stMetricValue"]{
    color:#fff!important;
    text-shadow:0 0 18px rgba(103,232,249,.22)
}

[data-testid="stDataFrame"]{
    border:1px solid rgba(167,139,250,.22);
    border-radius:16px;
    overflow:hidden
}

[data-testid="stExpander"]{
    background:rgba(13,9,28,.78);
    border:1px solid rgba(139,92,246,.22);
    border-radius:16px
}

hr{
    border-color:rgba(167,139,250,.14)!important
}

/* document preview */
.text-document{
    background:#fbfbfd;
    color:#17151d;
    border-radius:10px;
    padding:34px 40px;
    min-height:700px;
    white-space:pre-wrap;
    font-family:Georgia,serif;
    line-height:1.55;
    box-shadow:0 12px 35px rgba(0,0,0,.25);
    overflow:auto
}

.neon-pill{
    display:inline-flex;
    align-items:center;
    gap:8px;
    padding:7px 13px;
    border:1px solid rgba(103,232,249,.28);
    border-radius:999px;
    background:rgba(34,211,238,.06);
    color:#a5f3fc;
    font-size:.82rem;
    box-shadow:0 0 20px rgba(34,211,238,.08)
}

.neon-dot{
    width:7px;
    height:7px;
    border-radius:50%;
    background:#67e8f9;
    box-shadow:0 0 12px #67e8f9
}
</style>
""",
    unsafe_allow_html=True,
)


# ------------------------------- state

for key, default in {
    "results": None,
    "required_skills": [],
    "page": "Screening",
    "resume_bytes": {},
    "resume_names": {},
}.items():
    if key not in st.session_state:
        st.session_state[key] = default


# ------------------------------- navigation

st.markdown(
    '<div class="neon-pill">'
    '<span class="neon-dot"></span> '
    'AI Screening Engine · Ready'
    '</div>',
    unsafe_allow_html=True,
)

st.title("🧠 AI-Powered Resume Screening System")

st.caption(
    "A focused workspace for job-description analysis, "
    "candidate ranking, and resume review."
)


pages = ["Screening", "Ranked Candidates", "Candidate Details"]

nav_cols = st.columns(3)

for col, page in zip(nav_cols, pages):
    with col:
        if st.button(
            page,
            use_container_width=True,
            key=f"nav_{page}"
        ):
            st.session_state.page = page
            st.rerun()


st.divider()


# ------------------------------- screening page

if st.session_state.page == "Screening":

    st.subheader("Screening Workspace")

    st.caption(
        "Each input has its own workspace card. Complete the job "
        "description and upload resumes, then run the ranking engine."
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            '<div class="neon-card">'
            '<div class="card-icon">💼</div>'
            '<div class="card-title">Job Description</div>'
            '<div class="card-copy">'
            'Paste a job description or upload a PDF, DOCX, or TXT file.'
            '</div>'
            '<div class="card-status">INPUT · JD</div>'
            '</div>',
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            '<div class="neon-card">'
            '<div class="card-icon">📄</div>'
            '<div class="card-title">Candidate Resumes</div>'
            '<div class="card-copy">'
            'Upload one or more candidate resumes for batch screening.'
            '</div>'
            '<div class="card-status">INPUT · RESUMES</div>'
            '</div>',
            unsafe_allow_html=True,
        )

    with c3:
        st.markdown(
            '<div class="neon-card">'
            '<div class="card-icon">🧩</div>'
            '<div class="card-title">Skill Configuration</div>'
            '<div class="card-copy">'
            'Auto-detect skills from the JD or choose required skills manually.'
            '</div>'
            '<div class="card-status">CONFIG · SCORING</div>'
            '</div>',
            unsafe_allow_html=True,
        )

    st.write("")

    left, right = st.columns(2)

    jd_text = ""

    with left:
        st.markdown("### 01 · Job Description")

        jd_input_mode = st.radio(
            "Input method",
            ["Paste text", "Upload file"],
            horizontal=True,
            key="jd_mode",
        )

        if jd_input_mode == "Paste text":
            jd_text = st.text_area(
                "Paste the job description here",
                height=290,
                key="jd_text_area",
            )

        else:
            jd_file = st.file_uploader(
                "Upload JD (pdf, docx, txt)",
                type=["pdf", "docx", "txt"],
                key="jd_file",
            )

            if jd_file is not None:
                jd_text = extract_text(
                    jd_file.name,
                    io.BytesIO(jd_file.getvalue()),
                )

                st.text_area(
                    "Extracted JD text",
                    jd_text,
                    height=220,
                    disabled=True,
                )

    with right:
        st.markdown("### 02 · Candidate Resumes")

        resume_files = st.file_uploader(
            "Upload one or more resumes (pdf, docx, txt)",
            type=["pdf", "docx", "txt"],
            accept_multiple_files=True,
            key="resume_files",
        )

        if resume_files:
            st.success(
                f"{len(resume_files)} resume(s) ready"
            )

            for f in resume_files:
                st.write(f"• {f.name}")

    st.markdown("### 03 · Required Skills & Scoring")

    auto_skills = extract_skills(jd_text) if jd_text else []

    skill_mode = st.radio(
        "How should required skills be determined?",
        ["Auto-detect from JD", "Choose manually"],
        horizontal=True,
    )

    if skill_mode == "Auto-detect from JD":
        required_skills = auto_skills

        if jd_text:
            st.info(
                "Auto-detected skills: "
                + (
                    ", ".join(auto_skills)
                    if auto_skills
                    else "none found"
                )
            )

    else:
        required_skills = st.multiselect(
            "Select required skills",
            options=sorted(SKILLS_DB),
            default=auto_skills,
        )

    skill_weight = st.slider(
        "Weight given to skill-match vs. text similarity",
        0.0,
        1.0,
        0.4,
        0.05,
        help="0 = TF-IDF only. 1 = skill overlap only.",
    )

    if st.button(
        "🔍 Rank Candidates",
        type="primary",
        use_container_width=True,
    ):

        if not jd_text.strip():
            st.error("Please provide a job description.")

        elif not resume_files:
            st.error("Please upload at least one resume.")

        else:
            with st.spinner(
                "Extracting text and ranking candidates..."
            ):

                resumes = []
                bytes_map = {}
                names_map = {}

                for f in resume_files:

                    try:
                        data = f.getvalue()

                        text = extract_text(
                            f.name,
                            io.BytesIO(data),
                        )

                        resumes.append(
                            {
                                "filename": f.name,
                                "text": text,
                            }
                        )

                        bytes_map[f.name] = data
                        names_map[f.name] = f.name

                    except Exception as e:
                        st.warning(
                            f"Could not read {f.name}: {e}"
                        )

                results = rank_resumes(
                    jd_text,
                    resumes,
                    required_skills=required_skills or None,
                    skill_weight=skill_weight,
                )

                st.session_state.results = results
                st.session_state.required_skills = required_skills
                st.session_state.resume_bytes = bytes_map
                st.session_state.resume_names = names_map
                st.session_state.page = "Ranked Candidates"

                st.rerun()


# ------------------------------- ranked page

elif st.session_state.page == "Ranked Candidates":

    st.subheader("📊 Ranked Candidates")

    results = st.session_state.results

    if not results:
        st.info(
            "Run a screening first from the Screening page."
        )

    else:
        st.caption(
            "Candidates are ordered by the combined final score "
            "from text similarity and explicit skill matching."
        )

        table_data = [
            {
                "Rank": i + 1,
                "Candidate": r.candidate_name,
                "File": r.filename,
                "Final Score": r.final_score,
                "Text Similarity %": r.similarity_score,
                "Skill Match %": r.skill_match_percent,
                "Matched Skills": len(r.matched_skills),
                "Missing Skills": len(r.missing_skills),
            }
            for i, r in enumerate(results)
        ]

        df = pd.DataFrame(table_data)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
        )

        st.bar_chart(
            df.set_index("Candidate")["Final Score"]
        )

        st.download_button(
            "⬇️ Download results as CSV",
            df.to_csv(index=False).encode("utf-8"),
            "ranked_candidates.csv",
            "text/csv",
        )

        st.write("")

        if st.button(
            "🔎 Open Candidate Details",
            type="primary",
            use_container_width=True,
        ):
            st.session_state.page = "Candidate Details"
            st.rerun()


# ------------------------------- detail page

else:

    st.subheader("🔎 Candidate Details")

    results = st.session_state.results

    if not results:
        st.info(
            "Run a screening first from the Screening page."
        )

    else:

        selected_name = st.selectbox(
            "Select a candidate",
            [r.candidate_name for r in results],
        )

        selected = next(
            r for r in results
            if r.candidate_name == selected_name
        )

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Final Score",
            f"{selected.final_score}%"
        )

        c2.metric(
            "Text Similarity",
            f"{selected.similarity_score}%"
        )

        c3.metric(
            "Skill Match",
            f"{selected.skill_match_percent}%"
        )

        d1, d2 = st.columns(2)

        with d1:
            st.markdown("### ✅ Matched Skills")
            st.write(
                ", ".join(selected.matched_skills)
                or "None"
            )

        with d2:
            st.markdown("### ❌ Missing Skills")
            st.write(
                ", ".join(selected.missing_skills)
                or "None"
            )

        st.divider()

        st.markdown("### 📄 Original Resume Preview")

        file_data = st.session_state.resume_bytes.get(
            selected.filename
        )

        ext = selected.filename.lower().rsplit(
            ".",
            1
        )[-1]

        # FIXED PDF PREVIEW
        if file_data and ext == "pdf":
            st.pdf(
                file_data,
                height=900,
            )

        elif file_data and ext == "txt":

            safe = (
                selected.raw_text
                .replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
            )

            st.markdown(
                f'<div class="text-document">{safe}</div>',
                unsafe_allow_html=True,
            )

        else:

            st.info(
                "This file type cannot be rendered as an exact "
                "browser document preview here. Showing extracted "
                "content below."
            )

            safe = (
                selected.raw_text
                .replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
            )

            st.markdown(
                f'<div class="text-document">{safe}</div>',
                unsafe_allow_html=True,
            )

        with st.expander(
            "View extracted text used by the ranking engine"
        ):
            st.code(
                selected.raw_text[:10000],
                language="text",
            )
