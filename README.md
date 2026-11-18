# 🌱 Crop Recommendation System

An enterprise-grade, machine learning-powered **Crop Recommendation System** built with **Django**, **Scikit-Learn**, **Bootstrap 5**, and **Chart.js**[cite: 2, 4, 7]. The platform helps farmers and agronomists determine the optimal crop to cultivate based on soil macronutrients and micro-climate conditions.

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0+-092E20?style=for-the-badge&logo=django&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Random%20Forest-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![Chart.js](https://img.shields.io/badge/Chart.js-4.4-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white)

---

## 🚀 Key Features

### 👨‍🌾 Farmer / User Portal
* **Real-Time Crop Prediction Engine:** Predicts the best-suited crop out of 22+ varieties using a trained **Random Forest Classifier** (`Crop_recommendation_RF.pkl`).
* **7 Agronomic Input Metrics:** Analyzes **Nitrogen (N)**, **Phosphorus (P)**, **Potassium (K)**, **Temperature (°C)**, **Humidity (%)**, **Soil pH**, and **Rainfall (mm)**.
* **Random Sample Simulator:** One-click realistic soil and climate profile generator for rapid model testing.
* **Cloud Prediction History:** Automatically logs every prediction per user with individual record management.
* **Account & Security Management:** Full authentication flow (Sign Up, Login, Profile Update, and Secure Password Change).

### 🛡️ Enterprise Admin Dashboard
* **Executive KPI Telemetry:** Tracks total registered users, total predictions run, top recommended crop, and average user engagement rate[cite: 2].
* **Interactive Analytics (Chart.js):**
  * **Crop Recommendation Distribution:** Gradient bar chart displaying top predicted crops[cite: 2].
  * **Soil N-P-K Profile:** Radar chart visualizing mean soil macronutrient levels[cite: 2].
  * **Top Active Users:** Horizontal leaderboard of most active accounts[cite: 2].
  * **Climate & Soil pH Index:** Polar area breakdown of temperature, humidity, pH, and rainfall[cite: 2].
* **User & Audit Log Moderation:** Dedicated admin views to inspect and manage registered users and system-wide prediction records.

---

## 📂 Repository Structure

```text
Crop-Recommendation-Project/
├── crop_project/                  # Django web application
│   ├── crop_project/              # Project settings & root URLs
│   ├── recommender/               # Core app (views, models, forms, templates, static)
│   └── manage.py                  # Django CLI utility
├── CropRecommendation.ipynb       # Model training, EDA & evaluation notebook
├── Crop_recommendation.csv        # Agricultural dataset (N, P, K, temp, humidity, pH, rainfall)
└── Crop_recommendation_RF.pkl     # Serialized Random Forest ML model
