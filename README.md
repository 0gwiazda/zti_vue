## Instalation

backend:
*   cd ./backend/
*   python (python3) -m venv venv
*   (activate venv)
*   pip install -r ./requirements.txt
*   pip install uvicorn

frontend:
*   cd ./frontend/zti-sem-project
*   npm i

## Running

backend:
*   uvicorn main:app --reload --port 3000

frontend:
*   npm run serve