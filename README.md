# Python Project

## Motivation
Build an end to end python project with a set of established software project tools


## Components

|Component|Tool|Example|
|---|---|---|
|Language|Python|calculator.py|
|API&UI Framework|FastAPI| main.py|
|Linting|flake8||
|Unit Tests|pytest|tests/test_unit.py|
|Integration Tests|pytest|tests/test_integration.py|
|API Tests|pytest (client model)|tests/test_api.py|
|UI E2E Tests|Playwright/pytest|tests/test_ui.py|
|Containerization|Docker|Dockerfile|
|Image Repo|DockerHub|https://hub.docker.com/r/victorychang/calculator|


## Order
1. flake8 --max-line-length=127  calculator.py main.py tests/
2. pytest -rPx tests/test_unit.py
3. pytest -rPx tests/test_integration.py
4. uvicorn main:app --reload
5. pytest -rPx tests/test_api.py
6. pytest -rPx tests/test_ui.py
7. local build 
    1. docker build -t victorychang/calculator:1.0.0 .
    2. docker run -d --name my-calculator -p 8002:3000 victorychang/calculator:1.0.0
    1. view: http://127.0.0.1:8002/
8. write to DockerHub
    1. docker push victorychang/calculator:1.0.0
    2. docker pull victorychang/calculator:1.0.0
    3. docker run -d --name my-calculator -p 8002:3000 victorychang/calculator:1.0.0
    4. view: http://127.0.0.1:8002/
