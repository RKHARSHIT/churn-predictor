# 📈 Telecom Customer Churn Prediction

This project is an end-to-end machine learning pipeline to predict telecom customer churn. It covers exploratory analysis, feature engineering, model building, web app deployment using Flask, Dockerization, and cloud hosting via Render.

---

## 📁 Project Structure

```
D:/Project/
├── data/                         # Raw or preprocessed datasets
├── model/                        # Trained model and scaler files
│   ├── logistic_model.pkl
│   └── scaler.pkl
├── notebooks/                    # Jupyter notebooks for development
├── templates/                    # HTML templates for Flask frontend
│   └── form.html
├── render.yaml                   # Render config
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
- 🌐 Flask Web Interface for Predictions
- 🐳 Dockerized for Portability
- ⚙️ Docker Compose for Scaling
- ☁️ Deployed on [Render](https://churn-predictor-yngj.onrender.com)

---

## 🧪 ML Model Details

- **Algorithm**: Logistic Regression  
- **Preprocessing**: Standard Scaling, One-Hot Encoding, Feature Grouping  
- **Target Variable**: Customer Churn (Yes/No)

---

## 🚀 Run Locally (without Docker)

1. Clone the repository:
   ```bash
   git clone https://github.com/rkharshit/churn-predictor.git
   cd churn-predictor
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Launch the app:
   ```bash
   python app.py
   ```

4. Open in browser:
   ```
   http://127.0.0.1:5000/
   ```

---

## 🐳 Docker Instructions

### 🔨 Build Docker Image

```bash
docker build -t churn-predictor .
```

### 🚀 Run the Container

```bash
docker run -d --name churn_app -p 5000:5000 churn-predictor
```

---

## 📦 Docker Compose

For local orchestration:

```yaml
version: '3'
services:
  web:
    build: .
    ports:
      - "5000:5000"
```

Run it:

```bash
docker-compose up --build -d
```

---

## 🗃️ Push to GitHub Container Registry (GHCR)

1. Authenticate:
   ```bash
   echo <YOUR_FINE_GRAINED_PAT> | docker login ghcr.io -u rkharshit --password-stdin
   ```

2. Tag & Push:
   ```bash
   docker tag churn-predictor ghcr.io/rkharshit/churn-predictor:latest
   docker push ghcr.io/rkharshit/churn-predictor:latest
   ```

---

## 🌍 Render Deployment

**Live App**: [https://churn-predictor-yngj.onrender.com](https://churn-predictor-yngj.onrender.com)

### `render.yaml` Configuration

```yaml
services:
  - type: web
    name: churn-predictor
    env: docker
    repo: https://github.com/rkharshit/churn-predictor
    region: oregon
    plan: free
    branch: main
    dockerContext: .
    dockerfilePath: Dockerfile
    healthCheckPath: /
    envVars:
      - key: PORT
        value: 5000
```

---
## ✅ Final Deployment Checklist

- [x] Flask app built and running
- [x] Dockerized and tested locally
- [x] GitHub repo created and pushed
- [x] Docker image pushed to GHCR
- [x] Render deployment created and working
- [x] `render.yaml` configured
- [x] Project public at `https://churn-predictor-yngj.onrender.com`
- [x] README created and published

---

## 🙌 Credits

Project built by **[HARSHIT ARORA](https://github.com/rkharshit)**  

---

## 📬 Questions or Feedback?

Raise an issue in [GitHub Issues](https://github.com/rkharshit/churn-predictor/issues)