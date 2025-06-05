from fastapi import FastAPI, HTTPException, UploadFile, File, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .routes import login, employees

app = FastAPI(title="Sayonara API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login.router, prefix="/api")
app.include_router(employees.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Sayonara API"}
