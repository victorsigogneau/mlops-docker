from fastapi import FastAPI
from pymongo import MongoClient
import pandas as pd
import joblib
from pydantic import BaseModel

class InputData(BaseModel):
    bill_length_mm: float
    bill_depth_mm: float
    flipper_length_mm: float
    body_mass_g: float


client = MongoClient('mongo', 27017)
db = client.test_database
collection = db.test_collection
app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/add/{fruit}")
async def add_fruit(fruit: str):
    id = collection.insert_one({"fruit": fruit}).inserted_id
    return list(collection.find({}, {"_id": False}))

@app.get("/list")
async def list_fruits():
    fruits = list(collection.find({}, {"_id": False}))
    return fruits


@app.post("/predict")
async def predict(input_data: InputData):
    # Charger le modèle préalablement entraîné
    model = joblib.load('model.pkl')
    
    # Convertir les données d'entrée en DataFrame
    input_dict = input_data.dict()
    input_df = pd.DataFrame([input_dict])  # Convertir en DataFrame avec une seule ligne
    
    # Faire la prédiction
    prediction = model.predict(input_df)
    
    # Retourner le résultat
    return {"prediction": prediction[0]}



