from pydantic import BaseModel

class Employee(BaseModel):
    id: int
    nickname: str
    city: str
    deposit: int
    mk: str
