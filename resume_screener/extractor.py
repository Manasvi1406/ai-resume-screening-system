"""
extractor.py
------------
Utilities to pull raw text out of resumes in PDF, DOCX, or TXT format.
"""

import io
import re
from typing import Union

import docx2txt
from pypdf import PdfReader


def extract_text_from_pdf(file: Union[str, io.BytesIO]) -> str:
    """Extract raw text from a PDF file path or file-like object."""
    reader = PdfReader(file)
    text_parts = []
    for page in reader.pages:
        page_text = page.extract_text() or ""
        text_parts.append(page_text)
    return "\n".join(text_parts)


def extract_text_from_docx(file: Union[str, io.BytesIO]) -> str:
    """Extract raw text from a DOCX file path or file-like object."""
    return docx2txt.process(file) or ""


def extract_text_from_txt(file: Union[str, io.BytesIO]) -> str:
    """Extract raw text from a plain text file path or file-like object."""
    if isinstance(file, str):
        with open(file, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    raw = file.read()
    if isinstance(raw, bytes):
        return raw.decode("utf-8", errors="ignore")
    return raw


def extract_text(filename: str, file: Union[str, io.BytesIO]) -> str:
    """
    Dispatch to the correct extractor based on file extension.
    `filename` is used only to detect the extension; `file` is the path
    or an in-memory file-like object (e.g. from Streamlit's uploader).
    """
    ext = filename.lower().rsplit(".", 1)[-1]
    if ext == "pdf":
        text = extract_text_from_pdf(file)
    elif ext == "docx":
        text = extract_text_from_docx(file)
    elif ext == "txt":
        text = extract_text_from_txt(file)
    else:
        raise ValueError(f"Unsupported file type: .{ext} (use pdf, docx, or txt)")
    return clean_text(text)


def clean_text(text: str) -> str:
    """Normalize whitespace and strip odd control characters."""
    text = re.sub(r"[\r\t]+", " ", text)
    text = re.sub(r"\n{2,}", "\n", text)
    text = re.sub(r"[ ]{2,}", " ", text)
    return text.strip()
