📘 Mini Udemy – E-Learning Platform

A simplified Udemy-like platform built with Python (Django).
This project allows instructors to create courses & lessons, while students can register, enroll, and learn.


---

🚀 Features

👨‍🎓 User Authentication (Register/Login/Logout)

👨‍🏫 Instructors can create courses & lessons

📚 Students can view courses & lessons

🔐 Authentication & access control

🖥️ Django Admin panel for full management



---

🛠️ Tech Stack

Backend: Django, Python

Database: SQLite (default, can switch to PostgreSQL/MySQL)

Frontend: Django Templates, HTML, CSS

Auth: Django Authentication System



---

📂 Project Structure

mini_udemy/
│
├── manage.py
├── mini_udemy/           # project settings
│   ├── settings.py
│   ├── urls.py
│
├── accounts/             # authentication
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/accounts/
│       ├── login.html
│       ├── register.html
│
├── courses/              # courses & lessons
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/courses/
│       ├── course_list.html
│       ├── course_detail.html
│       ├── course_form.html
│       ├── lesson_detail.html


---

