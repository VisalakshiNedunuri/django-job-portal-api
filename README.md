# 🚀 Django Job Portal API

A RESTful Job Portal Backend built using **Django** and **Django REST Framework**.

This project provides APIs for recruiters and job seekers. Recruiters can create and manage job postings, while job seekers can browse and apply for jobs.

---

## 📌 Features

### 👤 Authentication

- User Registration
- User Login
- DRF Token Authentication
- Protected APIs
- Role-Based Access (Recruiter & Job Seeker)

---

### 💼 Job Management

- Create Job
- Update Job
- Delete Job
- View Job Details
- List All Jobs

---

### 🔍 Search & Filtering

- Search by Job Title
- Filter by Company
- Filter by Location
- Filter by Salary Range

---

### 📄 Applications

- Apply for Jobs
- Prevent Duplicate Applications
- View My Applications
- Recruiter Can View Applicants
- Recruiter Can Update Application Status

---

### 📚 Pagination

- Page Number Pagination
- Custom Page Size

---

## 🛠 Tech Stack

- Python
- Django
- Django REST Framework
- DRF Token Authentication
- SQLite
- Git
- GitHub
- Thunder Client

---

## 📂 Project Structure

```
django-job-portal-api/

├── users/
├── jobs/
├── applications/
├── job_portal/

├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/django-job-portal-api.git
```

### Move into Project

```bash
cd django-job-portal-api
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate
```

### Run Server

```bash
python manage.py runserver
```

---

## 📡 API Endpoints

### Authentication

| Method | Endpoint |
|---------|----------|
| POST | /register/ |
| POST | /login/ |

---

### Jobs

| Method | Endpoint |
|---------|----------|
| GET | /jobs/ |
| GET | /jobs/<id>/ |
| POST | /jobs/create/ |
| PUT | /jobs/<id>/update/ |
| DELETE | /jobs/<id>/delete/ |

---

### Applications

| Method | Endpoint |
|---------|----------|
| POST | /applications/apply/ |
| GET | /applications/my-applications/ |
| GET | /applications/job/<id>/ |
| PATCH | /applications/<id>/status/ |

---

## 🚀 Future Improvements

- PostgreSQL
- Docker
- Deployment
- Email Notifications
- Resume Upload
- Saved Jobs
- Swagger Documentation
- Unit Testing

---

## 👩‍💻 Author

**Visalakshi Nedunuri**

Python | Django | Django REST Framework

---

⭐ If you found this project useful, consider giving it a star.