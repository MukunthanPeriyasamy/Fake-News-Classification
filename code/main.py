import pickle
import re
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from fastapi import FastAPI
from pydantic import BaseModel


list_stopwords = stopwords.words('english')

porter_stem = PorterStemmer()

def stemming(content):
    stem_content = re.sub('[^a-zA-Z]', ' ', content) 
    stem_content = stem_content.lower()
    stem_content = stem_content.split()
    stem_content = [porter_stem.stem(word) for word in stem_content if word not in list_stopwords]
    stem_content = ' '.join(stem_content)
    return stem_content

model_path = 'model/model.pkl'
with open(model_path, 'rb') as f:
    model = pickle.load(f)

app = FastAPI()  

# (1) Define input schema
class NewsRequest(BaseModel):
    text: str

# (2) Create prediction endpoint
@app.post("/predict")
def predict(request: NewsRequest):
    pred = stemming(request.text)
    pred = model.predict([request.text])[0]
    prob = model.predict_proba([request.text]).max()
    return {"prediction": "Real" if int(pred) == 0 else "Fake", "confidence": round(float(prob) * 100,2)}

