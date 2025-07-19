# Python Project

## Motivation
Build an end to end python project with a set of established software project tools


## Components

|Component|Tool|Example|
|---|---|---|
|Language|Python|calculator.py|
|API&UI Framework|FastAPI| main.py|
|Unit Tests|pytest|tests/test_unit.py|
|Integration Tests|pytest|tests/test_integration.py|
|API Tests|pytest (client model)|tests/test_api.py|
|UI E2E Tests|pytest|tests/test_ui.py|


## Order
1. pytest -rPx tests/test_unit.py
2. pytest -rPx tests/test_integration.py
3. uvicorn main:app --reload
4. pytest -rPx tests/test_api.py
5. pytest -rPx tests/test_ui.py
