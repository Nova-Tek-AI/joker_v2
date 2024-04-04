from pydantic import BaseModel

class UserMessageInSchema(BaseModel):
    message: str