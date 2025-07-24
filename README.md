# ScanMyCV

#### Video Demo: [Insert your YouTube video link here]

#### Description:

**ScanMyCV** is a web-based resume analyzer developed as the final project for CS50x. This application allows users to upload their resumes and instantly receive a score out of 100, along with improvement suggestions based on structure, skills, readability, and formatting best practices.

Built using **Python (Flask)** for the backend and **HTML/CSS** for the frontend, ScanMyCV aims to help job seekers refine their resumes with clear, actionable feedback — quickly and for free.

---

### Key Features

- 📄 **Resume Upload** – Accepts `.pdf`, `.docx`, and `.txt` files.
- 🔍 **Text Extraction** – Parses uploaded files to extract readable text.
- 📊 **Scoring System** – Evaluates resumes on 5 main criteria:
  - Length
  - Skill Keywords
  - Readability
  - Section Formatting
  - Contact Info
- 💡 **Improvement Tips** – Suggests enhancements like adding missing sections, improving clarity, and fixing passive voice.
- 📥 **Downloads** – Users can download:
  - A list of suggestions
  - A polished resume template (`.docx` format)

---

### Technologies Used

- Python
- Flask
- HTML5 & CSS3
- PDFMiner (for PDF parsing)
- `textstat` (for readability scoring)

---

### Files Overview

- `app.py` – The Flask application and routing logic.
- `resume_utils.py` – Helper functions for text extraction and resume analysis.
- `templates/` – Contains `index.html` and `result.html` for the UI.
- `static/` – CSS and image assets.
- `uploads/` – Temporary folder for storing uploaded resumes.
- `Resume_Template_CS50.docx` – Sample resume template.

---

### Design Choices

- Simple, intuitive layout with emphasis on clarity.
- Focused on early-career and student-level resumes.
- Maintains server-side processing only — no cloud uploads or external API calls.
- Readability is based on Flesch Reading Ease, encouraging clarity in writing.

---

### Acknowledgments

This project was inspired by the CS50x final project guidelines and aims to solve a real-world problem for resume builders and students entering the job market.

> Created by [Malinga Sadharuwan](https://github.com/zukoo52)  
> CS50x 2025 — Sri Lanka 🇱🇰

---

