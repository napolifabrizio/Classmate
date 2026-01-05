from pydantic import BaseModel

class UserInputRag(BaseModel):
    Content: str
    Name: str
    Area: str
