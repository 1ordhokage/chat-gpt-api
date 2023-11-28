from datetime import datetime

from pydantic import BaseModel


class QuestionRequestSchema(BaseModel):
    content: str


class QuestionResponseSchema(BaseModel):
    id: int
    user_id: int
    content: str
    asked_at: datetime
