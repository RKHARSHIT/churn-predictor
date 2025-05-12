# Telecom Customer Churn Prediction

This project is an end-to-end machine learning application to predict telecom customer churn. It includes data preprocessing, feature engineering, model building, a web interface via Flask, and Docker containerization for deployment.

---

## 📁 Project Structure

```
D:/Project/
├── data/                         # Raw or preprocessed datasets
├── model/                        # Trained model and scaler files
│   ├── logistic_model.pkl
│   └── scaler.pkl
├── notebooks/                    # Jupyter notebooks for development
│              
├── templates/                    # HTML templates for Flask frontend
│   └── form.html
├── __pycache__/                  # Python cache
├── app.py                        # Flask application
├── Dockerfile                    # Docker build instructions
├── docker-compose.yml           # Docker Compose for scaling
├── requirements.txt             # Python dependencies
└── README.md                     # Project documentation
```

---

## 🔧 Features

- 📊 Data Exploration & Feature Engineering
- 🔍 Logistic Regression Model
- 🌐 Flask Web App for Real-Time Prediction
- 🐳 Dockerized for Portability
- ⚙️ Docker Compose for Scalable Deployment

---

## 🧪 ML Model Details

- Model: Logistic Regression  
- Preprocessing: Scaling + One-Hot Encoding + Feature Engineering  
- Target: Customer Churn (Yes/No)

---

## 🚀 How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/RKHARSHIT/churn-predictor.git
   cd churn-predictor
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the Flask app:
   ```bash
   python app.py
   ```

4. Go to `http://127.0.0.1:5000/` in your browser.

---

## 🐳 Docker Instructions

### 👉 Build Docker Image

```bash
docker build -t churn-predictor .
```

### 👉 Run Container

```bash
docker run -d --name churn_app -p 5000:5000 churn-predictor
```

---

## 🧱 Docker Compose

Use Docker Compose for orchestration:

```yaml
# docker-compose.yml
version: '3'
services:
  web:
    build: .
    ports:
      - "5000:5000"
```

Then run:

```bash
docker-compose up --build -d
```

---

## 📦 Publish to GitHub Container Registry

1. Login:
   ```bash
   echo $CR_PAT | docker login ghcr.io -u USERNAME --password-stdin
   ```

2. Tag and push:
   ```bash
   docker tag churn-predictor ghcr.io/USERNAME/churn-predictor
   docker push ghcr.io/USERNAME/churn-predictor
   ```

---
