from pydantic import BaseModel

class AddNewTokenSchemes(BaseModel):
    title: str
    token: str

class ReturnToken(AddNewTokenSchemes):
    id: int