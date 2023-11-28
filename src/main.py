from fastapi import FastAPI

from src.api.auth import router as auth_router
from src.api.questions import router as questoins_router
from src.api.users import router as users_router


app = FastAPI(
    title="Chat-GPT service",
    description="Chat-GPT twin app.",
    version="0.0.1"
)

app.include_router(auth_router)
app.include_router(questoins_router)
app.include_router(users_router)
