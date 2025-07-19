from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from calculator import double_sum, sum


app = FastAPI()


@app.get("/")
def home():
    return {"status": "healthy"}


@app.get("/api/v1/sum")
def get_sum(a: int, b: int):
    return sum(a, b)


@app.get("/api/v1/double_sum")
def get_double_sum(a: int, b: int):
    return double_sum(a, b)


@app.get("/ui/v1/sum", response_class=HTMLResponse)
def get_sum(a: int, b: int):
    return f"<div name=\"sum\" style=\"background-color: aqua\">{sum(a, b)}</div>"


@app.get("/ui/v1/double_sum", response_class=HTMLResponse)
def get_sum(a: int, b: int):
    return f"<div name=\"double_sum\" style=\"background-color: aqua\">{double_sum(a, b)}</div>"
