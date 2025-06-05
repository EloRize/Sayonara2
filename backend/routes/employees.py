from fastapi import APIRouter, HTTPException, UploadFile, File
from pydantic import BaseModel
from ..utils import excel
import os
import shutil

router = APIRouter()

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(DATA_DIR, exist_ok=True)

def employee_file(emp_id: int) -> str:
    return os.path.join(DATA_DIR, f"employee_{emp_id}", 'Кураторская.xlsx')

class Employee(BaseModel):
    id: int
    nickname: str
    city: str
    deposit: int
    mk: str

EMPLOYEES = [
    {"id": 1, "nickname": "Сакура", "city": "Севастополь", "deposit": 100000, "mk": "100г меф"},
    {"id": 2, "nickname": "Фудзияма", "city": "Москва", "deposit": 80000, "mk": "50г меф"}
]

@router.get('/employees')
def list_employees():
    return EMPLOYEES

@router.get('/employees/{emp_id}')
def get_employee(emp_id: int):
    for e in EMPLOYEES:
        if e['id'] == emp_id:
            return e
    raise HTTPException(status_code=404, detail='Employee not found')

@router.post('/employees/{emp_id}/spreadsheet')
def upload_spreadsheet(emp_id: int, file: UploadFile = File(...)):
    path = employee_file(emp_id)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'wb') as out:
        shutil.copyfileobj(file.file, out)
    return {"status": "uploaded"}

@router.get('/employees/{emp_id}/spreadsheet')
def download_spreadsheet(emp_id: int):
    path = employee_file(emp_id)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail='Spreadsheet not found')
    return excel.stream_excel(path)

@router.post('/employees/{emp_id}/upload-csv')
def upload_csv(emp_id: int, file: UploadFile = File(...)):
    path = employee_file(emp_id)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail='Spreadsheet not found')
    excel.process_csv(path, file)
    return {"status": "csv processed"}
