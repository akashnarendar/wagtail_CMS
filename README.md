# 🧠 AI Portfolio CMS — Built with Wagtail + Python + AWS

This project is a **production-ready AI Portfolio platform** designed to showcase end-to-end Machine Learning and Generative AI work — while itself acting as a demonstration of modern **Python full-stack engineering**.

---

## 🚀 Purpose

- 📂 Centralize and present real AI/ML/LLM projects
- 🧠 Highlight capabilities in LLMs, NLP, MLOps, and Generative AI
- 🛠 Showcase full-stack backend engineering using Django, Wagtail, and FastAPI
- ☁️ Deployed with Docker and AWS, CI/CD-enabled

This site serves as both a **professional portfolio** and an **example of production-quality CMS engineering** using Wagtail, with rich, dynamic project pages and clean layout.

---

## 🛠 Tech Stack

| Layer | Tools |
|------|-------|
| CMS & Backend | Wagtail, Django, Python 3.11 |
| Frontend UI | HTML + Wagtail Templates |
| AI Project Integration | Streamlit, FastAPI, Hugging Face, LangChain |
| Cloud Infrastructure | AWS ECS / Elastic Beanstalk, S3, Docker |
| CI/CD | GitHub Actions (build + deploy) |

---

## 💡 Features

- ✅ Custom project pages for every AI/ML application
- ✅ Clean, responsive design for blog-style writeups
- ✅ Rich content editing via Wagtail admin
- ✅ Navigation bar and footer for branding
- ✅ Ready for AWS deployment and GitHub CI/CD

---

## 📂 Directory Structure

├── Dockerfile ├── docker-compose.yml ├── requirements.txt ├── mysite/ # Wagtail/Django project ├── home/ # HomePage app (virtual CV) ├── projects/ # Project pages + index ├── templates/ │ ├── base.html │ └── home/ │ └── about_content.html │ └── projects/ │ ├── project_page.html │ └── projects_index_page.html ├── static/ ├── media/ └── README.md


---

## ▶️ Running Locally

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/ai-portfolio-wagtail.git
cd ai-portfolio-wagtail

# 2. Build and start the app
docker-compose up --build

# 3. Visit the site
http://localhost:8000

🧪 Wagtail Admin Login
docker-compose exec wagtail-web python manage.py createsuperuser

Then log in at:
http://localhost:8000/admin/

☁️ Deployment (AWS)
AWS ECS / Elastic Beanstalk ready via Docker

Static/media served via S3

CI/CD integrated using GitHub Actions:

    -Builds container

    -Pushes to ECR or EB

    -Deploys on push to main

📸 Sample Projects on This Site
InsightFlow — Autonomous research assistant using LangGraph, GPT-4

Sentiment Analyzer — ML pipeline with Hugging Face + Airflow

CV QnA Bot — Semantic resume search using FAISS + FastAPI

Want to view them live? Visit /projects/ once deployed!

🙌 Author
Narendar Punithan
Senior Data Scientist | AI/ML Engineer | Python Developer
📧 akashnarendar2013@gmail.com

🏁 License
This project is open source and intended for portfolio & educational use.

---