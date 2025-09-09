from fastapi import FastAPI

app = FastAPI(title="Taller8 API", version="1.0.0")

@app.get("/")
def root():
    return {"status": "ok", "service": "bankchurn-api"}

@app.post("/api/v1/predict")
def predict():
    # Ejemplo mínimo para el pantallazo 17
    return {"prediction": 1}
