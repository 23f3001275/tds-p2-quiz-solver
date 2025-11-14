from fastapi import APIRouter, HTTPException
from src.api.models import SolveRequest
from src.solver.fetcher import fetch_quiz_page
from src.solver.parser import parse_quiz
from src.solver.llm_planner import interpret_task
from src.solver.executor import execute_task
from src.solver.submitter import submit_answer
from src.utils.timing import timer

router = APIRouter()

VALID_SECRET = "your-secret"   # replace with your own

@router.post("/solve")
@timer
async def solve_quiz(req: SolveRequest):

    if req.secret != VALID_SECRET:
        raise HTTPException(status_code=403, detail="Invalid secret")

    # Step 1: fetch HTML
    html, context = await fetch_quiz_page(req.url)

    # Step 2: parse HTML → extract question, submit_url, data refs
    question, submit_url, resources = parse_quiz(html)

    # Step 3: LLM → interpret question into a structured plan
    plan = await interpret_task(question, resources)

    # Step 4: execute instructions (data loading, processing)
    answer = await execute_task(plan, resources)

    # Step 5: POST to submit URL
    result = await submit_answer(submit_url, req, answer)

    return {
        "your_answer": answer,
        "server_reply": result
    }
