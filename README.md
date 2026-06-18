# 📝 Todo API (Django REST Framework)

[![Python](https://img.shields.io/badge/Python-3.13+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![Django](https://img.shields.io/badge/Django-5.0+-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com)
[![DRF](https://img.shields.io/badge/Django_REST_Framework-Redirection-Red?style=for-the-badge&logo=django&logoColor=white)](https://www.django-rest-framework.org)

A robust, highly scalable, and secure RESTful API for a Todo application, architected using **Python** and **Django REST Framework (DRF)**. This system enables full relational CRUD performance with state-of-the-art user isolation and token-based authentication protocols.

---

## 🚀 Architectural Features

* 🔐 **Secure User Authentication:** Built-in secure registration and token-based validation pipelines for user login.
* ⚡ **Full CRUD Ecosystem:** Optimized endpoints to Create, Read, Update, and Delete operational tasks.
* 📋 **Advanced Task Management:** Status toggles for task completion, priority metrics, and detailed text attributes.
* 🛡️ **Strict User Isolation:** Built-in permission classes ensuring users can strictly view, manipulate, or delete *only their own* personal datasets.
* 🖥️ **Browsable API Engine:** Fully documented and testable API playground via the native Django REST Framework interface.

---

## 🛠️ System Tech Stack

| Layer | Component | Description |
| :--- | :--- | :--- |
| **Language** | Python 3.13+ | Core execution runtime |
| **Framework** | Django / DRF | Web framework and serialization architecture |
| **Database** | SQLite3 | Local storage & development dataset testing |

---

## 🛣️ Production API Endpoints

| Method | Endpoint | Description | Authentication |
| :--- | :--- | :--- | :--- |
| **POST** | `/api/auth/register/` | Register a new user profile | None |
| **POST** | `/api/auth/login/` | Authenticate user & retrieve Token | None |
| **GET** | `/api/todos/` | List all todos for active user | Required |
| **POST** | `/api/todos/` | Ingest and create a new todo | Required |
| **GET** | `/api/todos/<id>/` | Fetch specific data for a single todo | Required |
| **PUT** | `/api/todos/<id>/` | Overwrite/Update a specific todo item | Required |
| **DELETE**| `/api/todos/<id>/` | Delete an existing todo dataset | Required |

---

## 🛠️ Environment Configuration & Deployment Setup

Follow this sequence to initialize your environment, install dependencies, map schemas, and broadcast the local build.

| Step | Phase | Execution Command | Technical Scope |
| :--- | :--- | :--- | :--- |
| **01** | **Environment Activation** | `python -m venv myenv`<br>`source myenv/Scripts/activate` | Initialize and activate isolated Python environment (Windows Build) |
| **02** | **Dependency Configuration** | `pip install django djangorestframework` | Install the required framework wrappers and core extensions |
| **03** | **Database Migrations** | `python manage.py migrate` | Compile and execute database schemas into the local engine |
| **04** | **Server Deployment** | `python manage.py runserver 0.0.0.0:8000` | Deploy the asynchronous development testing build |

---

### 🌐 Live API Telemetry Gateway
Once initialization completes, access the browsable REST playground at:
👉 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**
