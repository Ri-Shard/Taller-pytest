from main import *
from fastapi.testclient import TestClient
from main import app


client = TestClient(app)
def test_isPrime_test():
    assert is_prime(1)==False

def test_fibonacci_test():
    assert fibonacci(8)==21

def test_is_prime_endpoint():
    response = client.get("/IsPrime/4")
    assert response.status_code == 200
    assert response.json() == False
    
    response = client.get("/IsPrime/2")
    assert response.status_code == 200
    assert response.json() == True