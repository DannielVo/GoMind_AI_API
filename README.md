# GoMind AI API

GoMind AI API is a Python-based backend built with **FastAPI** for GoMind AI, a web-based 9×9 Go game where players compete against an AI opponent.

The backend is designed to handle Go game rules, game state management, and AI decision-making using **Minimax Search with Alpha-Beta Pruning** and heuristic evaluation. It provides RESTful APIs for communication with the Next.js frontend.

The project follows a lightweight layered architecture, separating API routing, game logic, AI algorithms, and business services for maintainability and testing.

## Tech Stack

- **Language:** Python 3.11
- **Framework:** FastAPI
- **ASGI Server:** Uvicorn
- **Data Validation:** Pydantic
- **Testing:** Pytest, HTTPX
- **AI Algorithms:** Minimax Search, Alpha-Beta Pruning, Heuristic Evaluation
- **API Documentation:** Swagger UI (OpenAPI)

## Project Structure

```text
GoMind_AI_API/
├── app/
│   ├── main.py                 # FastAPI application entry point
│   ├── api/                    # API endpoints and routing
│   ├── core/                   # Application configuration and game engine
│   ├── ai/                     # AI algorithms and board evaluation
│   ├── schemas/                # Pydantic request/response schemas
│   ├── services/               # Game orchestration and session management
│   └── exceptions/             # Custom game exceptions
├── tests/                      # Automated tests
├── .env.example
├── .gitignore
├── pyproject.toml
└── README.md
```

_Note: `__init__.py` files and local environment files are omitted for readability._

## Getting Started

### Prerequisites

Make sure the following tools are installed:

- Python 3.11
- pip
- Git

### Steps

**1. Clone the repository**

```bash
git clone <repository-url>
cd GoMind_AI_API
```

**2. Create a virtual environment**

```cmd
py -3.11 -m venv .venv
```

**3. Activate the virtual environment**

Windows (CMD):

```cmd
.venv\Scripts\activate.bat
```

Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
source .venv/bin/activate
```

**4. Install dependencies**

```bash
python -m pip install -e ".[dev]"
```

**5. Configure environment variables**

Copy `.env.example` to `.env`:

Windows (CMD):

```cmd
copy .env.example .env
```

macOS / Linux:

```bash
cp .env.example .env
```

Update the environment variables as needed.

**6. Run the development server**

```bash
python -m uvicorn app.main:app --reload
```

The backend will be available at:

```text
http://127.0.0.1:8000
```

**7. Access API documentation**

FastAPI automatically generates interactive API documentation:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc
- **OpenAPI Schema:** http://127.0.0.1:8000/openapi.json

**8. Run tests**

```bash
python -m pytest tests/ -v
```
