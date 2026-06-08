from fastapi import FastAPI

app = FastAPI(
    title="Temporal Genome Agents",
    version="0.1.0",
)


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "framework": "TGA",
    }