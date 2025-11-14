from fastapi import FastAPI
from src.api.server import router as api_router

app = FastAPI(title="LLM Analysis Quiz Solver")
app.include_router(api_router)
