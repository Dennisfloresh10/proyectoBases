from fastapi import FastAPI

app = FastAPI(
    title="Sistema GBOX Casilleros Honduras",
    description="API logística tipo casillero Miami - Honduras",
    version="1.0"
)

@app.get("/")
def home():
    return {"message": "GBOX API funcionando correctamente"}