import httpx

async def submit_answer(url: str, req, answer):
    payload = {
        "email": req.email,
        "secret": req.secret,
        "url": req.url,
        "answer": answer
    }

    async with httpx.AsyncClient() as client:
        r = await client.post(url, json=payload)
        return r.json()
