from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from jinja2 import Environment, FileSystemLoader

app = FastAPI(title="PULSAR BOYC Information Service")

# Setup Jinja2 for templating
env = Environment(loader=FileSystemLoader("templates"))


@app.get("/", response_class=HTMLResponse)
async def root():
    """Display a welcome page with dummy PULSAR BOYC information."""
    template = env.get_template("index.html")
    content = template.render(
        title="PULSAR BOYC - SimpleVM Information",
        welcome_message="Welcome to the PULSAR BOYC Information Service",
        description="This service provides retrieval of PULSAR BOYC related information shown in FORC of SimpleVM for BOYC Clusters.",
        dummy_data={
            "total_clusters": 12,
            "active_clusters": 10,
            "total_nodes": 256,
            "cpu_cores": 2048,
            "total_memory_gb": 8192,
            "storage_tb": 500,
        },
    )
    return HTMLResponse(content=content)


@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring."""
    return {"status": "healthy", "service": "pulsar-boyc-info"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)