from fastapi import FastAPI

app = FastAPI(title="AI Ops Assistant - AI Service")

@app.get("/health")
def health_check():
    """
    Health check endpoint.
    """
    return {"status": "ok"}

@app.post("/chat")
def chat():
    """
    Placeholder endpoint to integrate LLM + RAG pipeline.
    """
    return {
        "message": "Chat endpoint is working",
        "data": None
    }    