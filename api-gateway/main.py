from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import jwt
import os
import subprocess
import requests
import ssl
import certifi

app = FastAPI()
SECRET_KEY = os.getenv("JWT_SECRET", "supersecretkey")

class User(BaseModel):
    username: str
    subdomain: str
    schema_name: str

class Pipeline(BaseModel):
    service: str
    version: str

# JWT Authentication
async def authenticate(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Set SSL Context for requests
session = requests.Session()
session.verify = certifi.where()

@app.post("/register-user")
async def register_user(user: User, token: str = Depends(authenticate)):
    try:
        response = session.post("http://db-service/create-schema", json=user.dict())
        response.raise_for_status()
        return {"message": "User registered successfully"}
    except requests.RequestException:
        raise HTTPException(status_code=500, detail="Schema creation failed")

@app.post("/trigger-pipeline")
async def trigger_pipeline(pipeline: Pipeline, token: str = Depends(authenticate)):
    try:
        result = subprocess.run([
            "curl", "-X", "POST", f"https://api.github.com/repos/username/{pipeline.service}/dispatches"],
            check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"message": f"{pipeline.service} pipeline triggered", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Pipeline trigger failed: {e.stderr.decode()}")

@app.post("/rollback")
async def rollback(pipeline: Pipeline, token: str = Depends(authenticate)):
    try:
        result = subprocess.run([
            "curl", "-X", "POST", f"https://api.github.com/repos/username/{pipeline.service}/rollback"],
            check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"message": f"Rollback for {pipeline.service} triggered", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Rollback failed: {e.stderr.decode()}")
