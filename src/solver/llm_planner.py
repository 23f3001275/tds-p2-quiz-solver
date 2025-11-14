import openai

async def interpret_task(question: str, resources: dict):
    prompt = f"""
    You are a task planner. Convert this question into a Python-executable plan.
    Return JSON only.

    Question:
    {question}
    """

    response = openai.chat.completions.create(
        model="gpt-5-nano",
        messages=[{"role": "user", "content": prompt}]
    )

    plan = response.choices[0].message["content"]
    return plan
