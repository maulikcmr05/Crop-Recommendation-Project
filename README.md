# 🌱 Crop Recommendation System

An enterprise-grade, machine learning-powered **Crop Recommendation System** built with **Django**, **Scikit-Learn**, **Bootstrap 5**, and **Chart.js**. The platform helps farmers and agronomists determine the optimal crop to cultivate based on soil macronutrients and micro-climate conditions.

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0+-092E20?style=for-the-badge&logo=django&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Random%20Forest-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![Chart.js](https://img.shields.io/badge/Chart.js-4.4-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white)

---

## 📋 Table of Contents
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Repository Structure](#-repository-structure)
- [Prerequisites](#-prerequisites)
- [Step-by-Step Installation & Setup](#-step-by-step-installation--setup)
- [Usage Guide](#-usage-guide)
- [Input Parameters & Ranges](#-input-parameters--ranges)
- [Troubleshooting](#-troubleshooting)
- [Author](#-author)

---

## 🚀 Key Features

### 👨‍🌾 Farmer / User Portal
* **Real-Time Crop Prediction Engine:** Predicts the best-suited crop out of 22+ varieties using a trained **Random Forest Classifier** (`Crop_recommendation_RF.pkl`).
* **7 Agronomic Input Metrics:** Analyzes **Nitrogen (N)**, **Phosphorus (P)**, **Potassium (K)**, **Temperature (°C)**, **Humidity (%)**, **Soil pH**, and **Rainfall (mm)**.
* **Random Sample Simulator:** One-click realistic soil and climate profile generator for rapid model testing.
* **Cloud Prediction History:** Automatically logs every prediction per user with individual record management.
* **Account & Security Management:** Full authentication flow (Sign Up, Login, Profile Update, and Secure Password Change).

### 🛡️ Enterprise Admin Dashboard
* **Executive KPI Telemetry:** Tracks total registered users, total predictions run, top recommended crop, and average user engagement rate.
* **Interactive Analytics (Chart.js):**
  * **Crop Recommendation Distribution:** Gradient bar chart displaying top predicted crops.
  * **Soil N-P-K Profile:** Radar chart visualizing mean soil macronutrient levels.
  * **Top Active Users:** Horizontal leaderboard of most active accounts.
  * **Climate & Soil pH Index:** Polar area breakdown of temperature, humidity, pH, and rainfall.
* **User & Audit Log Moderation:** Dedicated admin views to inspect and manage registered users and system-wide prediction records.

---

## 💻 Tech Stack

* **Backend:** Python, Django Framework
* **Machine Learning:** Scikit-Learn (Random Forest Classifier), Pandas, NumPy, Joblib
* **Frontend:** HTML5, CSS3, Bootstrap 5.3, Font Awesome 7, SweetAlert2, Chart.js 4
* **Database:** SQLite3 (Django Default ORM)

---

## 📂 Repository Structure

```text
Crop-Recommendation-Project/
├── crop_project/                  # Django web application root
│   ├── crop_project/              # Project settings, WSGI/ASGI & root URLs
│   ├── recommender/               # Core application
│   │   ├── migrations/            # Database schema migrations
│   │   ├── static/                # CSS stylesheets and UI images
│   │   ├── templates/             # HTML templates (User & Admin portals)
│   │   ├── models.py              # UserProfile & Prediction database models
│   │   ├── views.py               # Authentication, ML inference & Admin analytics logic
│   │   └── urls.py                # Application URL routing
│   ├── db.sqlite3                 # SQLite database
│   └── manage.py                  # Django CLI utility
├── CropRecommendation.ipynb       # Model training, EDA & evaluation notebook
├── Crop_recommendation.csv        # Agricultural dataset (N, P, K, temp, humidity, pH, rainfall)
└── Crop_recommendation_RF.pkl     # Serialized Random Forest ML model
```

---

## ⚙️ Prerequisites

Before running this project locally, ensure you have the following installed:
* **Python 3.10 or higher** ([Download Python](https://www.python.org/downloads/))
* **pip** (Python package manager)
* **Git** ([Download Git](https://git-scm.com/downloads))

---

## 🛠️ Step-by-Step Installation & Setup

### 1. Clone the Repository
Open your terminal or command prompt and run:
```bash
git clone https://github.com/maulikcmr05/Crop-Recommendation-Project.git
cd Crop-Recommendation-Project
```

### 2. Create & Activate a Virtual Environment
Creating a virtual environment isolates project dependencies:

* **Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
* **macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Required Dependencies
Install Django and the machine learning libraries:
```bash
pip install django scikit-learn pandas numpy joblib
```
> **Note:** Ensure your local `scikit-learn` version matches the version used to train `Crop_recommendation_RF.pkl` in `CropRecommendation.ipynb` to avoid serialization warnings.

### 4. Navigate to the Django Project Directory
```bash
cd crop_project
```

### 5. Apply Database Migrations
Initialize the SQLite database tables (`auth_user`, `UserProfile`, `Prediction`):
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create an Admin (Superuser) Account
Create staff credentials to access the **Admin Analytics Dashboard**:
```bash
python manage.py createsuperuser
```
Follow the prompts to enter a **Username**, **Email**, and **Password**.

### 7. Start the Development Server
```bash
python manage.py runserver
```
Once running, open your browser and visit:
* **Home Page:** `http://127.0.0.1:8000/`
* **User Prediction Portal:** `http://127.0.0.1:8000/recommender/predict/`
* **Custom Admin Dashboard:** `http://127.0.0.1:8000/recommender/admin-login/`

---

## 📖 Usage Guide

### 1. For Farmers / Users
* Click **Sign Up** to register with your Full Name, Email, Phone Number, and Password.
* Navigate to **Prediction**, enter your soil test values (or click **Random Sample** to auto-fill realistic metrics), and click **Run Prediction**.
* View all past predictions anytime under the **History** tab.

### 2. For Administrators
* Click **Admin** in the top navigation bar and sign in using your `createsuperuser` credentials.
* Monitor real-time crop trends, soil N-P-K averages, active users, and system-wide prediction logs on the **Dashboard**.

---

## 📊 Input Parameters & Ranges

| Parameter | Unit | Typical Range | Agronomic Role |
| :--- | :---: | :---: | :--- |
| **Nitrogen (N)** | mg/kg | 0 – 140 | Promotes leafy vegetative growth and chlorophyll synthesis |
| **Phosphorus (P)** | mg/kg | 5 – 145 | Supports root development, flowering, and seed formation |
| **Potassium (K)** | mg/kg | 5 – 205 | Enhances drought tolerance and overall plant immunity |
| **Temperature** | °C | 8 – 44 | Governs germination rate and metabolic activity |
| **Humidity** | % | 14 – 100 | Controls transpiration and moisture balance |
| **Soil pH** | pH | 3.5 – 9.5 | Determines nutrient availability in soil (6.0–7.5 optimal) |
| **Rainfall** | mm | 20 – 300+ | Defines seasonal water supply suitability |

---

## 🔧 Troubleshooting

* **Static files / CSS not updating:** Perform a hard refresh in your browser using `Ctrl + Shift + R` (Windows/Linux) or `Cmd + Shift + R` (macOS).
* **Model file (`Crop_recommendation_RF.pkl`) not found:** Verify that `Crop_recommendation_RF.pkl` is located in the root `Crop-Recommendation-Project/` directory (one level above `manage.py`) or update the model path in `recommender/views.py`.
* **Port 8000 already in use:** Run the server on a different port:
  ```bash
  python manage.py runserver 8080
  ```

---

link:[https://crop-recommendation-project-yjnj.onrender.com](https://crop-recommendation-project-yjnj.onrender.com)

## 👤 Author

**Maulik Patel**  
GitHub: [@maulikcmr05](https://github.com/maulikcmr05)
