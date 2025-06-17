from pydantic import BaseModel

class Update_user(BaseModel):
    user_id: int
    name: str 
    user_name: str
    phone_number: str | None=None
    email: str | None=None
    role: str 
