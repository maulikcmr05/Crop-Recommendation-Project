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

⚙️ Prerequisites
Before running this project locally, ensure you have the following installed:

Python 3.10 or higher (Download Python)

pip (Python package manager)

Git (Download Git)

🛠️ Step-by-Step Installation & Setup
1. Clone the Repository
Open your terminal or command prompt and run:

Bash
git clone [https://github.com/maulikcmr05/Crop-Recommendation-Project.git](https://github.com/maulikcmr05/Crop-Recommendation-Project.git)
cd Crop-Recommendation-Project
```[cite: 7]

### 2. Create & Activate a Virtual Environment
Creating a virtual environment isolates project dependencies:

* **Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
macOS / Linux:

Bash
python3 -m venv venv
source venv/bin/activate
3. Install Required Dependencies
Install Django and the machine learning libraries:

Bash
pip install django scikit-learn pandas numpy joblib
(Tip: Ensure your local scikit-learn version matches the version used to train Crop_recommendation_RF.pkl in CropRecommendation.ipynb to avoid serialization warnings[cite: 7].)

4. Navigate to the Django Project Directory
Bash
cd crop_project
```[cite: 4, 7]

### 5. Apply Database Migrations
Initialize the SQLite database tables (`auth_user`, `UserProfile`, `Prediction`):
```bash
python manage.py makemigrations
python manage.py migrate
6. Create an Admin (Superuser) Account
Create staff credentials to access the Admin Analytics Dashboard:

Bash
python manage.py createsuperuser
Follow the prompts to enter a Username, Email, and Password.

7. Start the Development Server
Bash
python manage.py runserver
Once running, open your browser and visit:

Home Page: http://127.0.0.1:8000/

User Prediction Portal: http://127.0.0.1:8000/recommender/predict/   
image_507bc0.png
+ 1

Custom Admin Dashboard: http://127.0.0.1:8000/recommender/admin-login/

📖 Usage Guide
For Farmers / Users:

Click Sign Up to register with your Full Name, Email, Phone Number, and Password.

Navigate to Prediction, enter your soil test values (or click Random Sample to auto-fill realistic metrics), and click Run Prediction.   
image_51cd05.jpg

View all past predictions anytime under the History tab.

For Administrators:

Click Admin in the top navigation bar and sign in using your createsuperuser credentials.   
image_51d121.jpg

Monitor real-time crop trends, soil N-P-K averages, active users, and system-wide prediction logs on the Dashboard[cite: 2].

📊 Input Parameters & Ranges
Parameter	Unit	Typical Range	Agronomic Role
Nitrogen (N)	mg/kg	0 – 140	
Promotes leafy vegetative growth and chlorophyll synthesis 
image_51cd05.jpg

Phosphorus (P)	mg/kg	5 – 145	
Supports root development, flowering, and seed formation[cite: 5]

Potassium (K)	mg/kg	5 – 205	
Enhances drought tolerance and overall plant immunity[cite: 5]

Temperature	°C	8 – 44	Governs germination rate and metabolic activity
Humidity	%	14 – 100	Controls transpiration and moisture balance
Soil pH	pH	3.5 – 9.5	
Determines nutrient availability in soil (6.0–7.5 optimal)[cite: 5]

Rainfall	mm	20 – 300+	Defines seasonal water supply suitability
🔧 Troubleshooting
Static files / CSS not updating: Perform a hard refresh in your browser using Ctrl + Shift + R (Windows/Linux) or Cmd + Shift + R (macOS).

Model file (Crop_recommendation_RF.pkl) not found: Verify that Crop_recommendation_RF.pkl is located in the root Crop-Recommendation-Project/ directory (one level above manage.py) or update the model path in recommender/views.py[cite: 4, 7].

Port 8000 already in use: Run the server on a different port:

Bash
python manage.py runserver 8080
👤 Author
Maulik Patel

GitHub: @maulikcmr05[cite: 7]
