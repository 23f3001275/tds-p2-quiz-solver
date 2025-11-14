import pandas as pd
import numpy as np
import json
import base64
import io
import matplotlib.pyplot as plt

async def execute_task(plan_json: str, resources: dict):

    plan = json.loads(plan_json)

    op = plan.get("operation")
    col = plan.get("column")

    # Example: simple sum
    if op == "sum":
        csv_url = plan["csv_url"]
        df = pd.read_csv(csv_url)
        return float(df[col].sum())

    # Example: chart creation
    if op == "plot":
        df = pd.read_csv(plan["csv_url"])
        img = io.BytesIO()
        df.plot(kind="bar")
        plt.savefig(img, format="png")
        img.seek(0)
        return "data:image/png;base64," + base64.b64encode(img.read()).decode()

    # fallback
    return {"plan": plan}
