from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
from app.logger import setup_logger

logger = setup_logger()
app = FastAPI(title="Agentic Coding Mentor API")

class CodeSnippet(BaseModel):
    code: str

model = pipeline("text2text-generation", model="Salesforce/codet5-base")

@app.post("/feedback")
def generate_feedback(snippet: CodeSnippet):
    try:
        logger.info("Received code snippet.")
        output = model(snippet.code)[0]['generated_text']
        return {"feedback": output}
    except Exception as e:
        logger.error(f"Error generating feedback: {e}")
        raise HTTPException(status_code=500, detail="Model inference failed.")
