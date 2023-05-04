from fastapi import FastAPI
from math import sqrt

app = FastAPI()

@app.get("/hello")
def hello():
    return "Hello FastAPI"

@app.get("/IsPrime/{num}")
def is_prime(num: int):
    if num < 2:
        return False
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True