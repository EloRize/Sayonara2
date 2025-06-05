from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post('/login')
def login(req: LoginRequest):
    if req.username == 'Tony' and req.password == '123':
        return {"status": "ok", "username": req.username}
    raise HTTPException(status_code=401, detail="Invalid credentials")
