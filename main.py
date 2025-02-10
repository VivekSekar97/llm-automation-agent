from fastapi import FastAPI, HTTPException
import os

app = FastAPI()

# Root endpoint to verify API is running
@app.get("/")
def read_root():
    return {"message": "LLM Automation Agent API is running!"}

# Endpoint to process tasks
@app.post("/run")
async def run_task(task: str):
    try:
        result = process_task(task)
        return {"status": "success", "result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
def process_task(task: str):
    # This is a placeholder, we'll add actual logic later
    return f"Task received: {task}"

