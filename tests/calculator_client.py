import requests


class CalculatorClient:
    def __init__(self):
        self.base_url = "http://127.0.0.1:8000"

    def get_health(self):
        return requests.get(self.base_url)

    def get_sum(self, a: int, b: int):
        return requests.get(f"{self.base_url}/api/v1/sum", params={"a": a, "b": b})

    def get_double_sum(self, a: int, b: int):
        return requests.get(f"{self.base_url}/api/v1/double_sum", params={"a": a, "b": b})
