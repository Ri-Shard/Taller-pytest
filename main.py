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

@app.get("/fibonacci/{pos}")
def fibonacci(pos: int):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(2, pos+1):
            c = a + b
            a = b
            b = c
        return b