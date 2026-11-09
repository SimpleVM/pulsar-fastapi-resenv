# simplevm-pulsar-fastapi

Webservice for retrieval of PULSAR BOYC related information shown in FORC of SimpleVM for BOYC Clusters.

## Quick Start

```bash
# Create and activate virtual environment
python3 -m venv vendor
source vendor/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python -m app.main
```

The application will be available at `http://localhost:8000`

## API Endpoints

- `GET /` - Main HTML page
- `GET /health` - Health check endpoint
- `GET /docs` - Auto-generated API documentation (Swagger UI)

## Project Structure

```
simplevm-pulsar-fastapi/
├── app/
│   └── main.py          # FastAPI application
├── templates/
│   └── index.html       # Main HTML template
├── requirements.txt     # Python dependencies
└── README.md
```