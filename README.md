# Fake News Classification

This repository provides a complete machine learning solution for detecting fake news articles using traditional ML methods and text processing on English (and optionally Tamil) datasets. Designed for extensibility, deployment, and easy API access.

## Features

- **Data Preprocessing**: Cleans, tokenizes, and vectorizes news headlines and text for ML.
- **Model Training & Evaluation**: Implements and compares multiple classifiers including Logistic Regression, Decision Tree, Random Forest, SVM, and KNN, with cross-validation.
- **Hyperparameter Tuning**: Uses GridSearchCV to find optimal model parameters.
- **API Hosting**: FastAPI backend for serving predictions.
- **Deployment Ready**: Dockerfile and requirements.txt included for seamless cloud/containerized deployment.
- **Extendable**: Separate `code/`, `model/`, and `dataset/` directories for collaboration and upgrades.
- **Written in Python**.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/MukunthanPeriyasamy/Fake-News-Classification.git
cd Fake-News-Classification
```

### 2. Environment Setup

Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Train or Use Existing Model

- To train from scratch, run/modify `model.ipynb`.
- To serve predictions, use the FastAPI app (`main.py`)
- Existing trained model is available at `model/model.pkl`.

### 4. Serve as API (FastAPI)

```bash
uvicorn model.main:app --reload --host 0.0.0.0 --port 8000
```
API endpoint will be available at: `http://localhost:8000/predict`

### 5. Deploy with Docker

Build and run the Docker container:

```bash
docker build -t fake-news-api .
docker run -p 8000:8000 fake-news-api
```

### 6. Example API Usage

Send a POST request:

```json
POST /predict
{
  "text": "Sample news headline here."
}
```

Response:
```json
{
  "prediction": Real,      
  "confidence": 0.98
}
```

## Author

Mukunthan Periyasamy
