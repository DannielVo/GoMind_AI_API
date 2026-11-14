from fastapi import FastAPI

app = FastAPI(
    title="GoMind AI API",
    description="Backend API for GoMind AI Go Game",
    version="1.0.0",
)


@app.get("/")
def root():
    return {"message": "Welcome to GoMind AI API"}


@app.get("/api/v1/health")
def health_check():
    return {"status": "ok"}