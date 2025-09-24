from .calculator_4 import Calculator4
from src.drivers.numpy_handler import NumpyHandler
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from typing import Dict, List
from pytest import raises


class MockRequest:
    def __init__(self, body: Dict) ->None:
        self.json = body

class MockDriverHandler:
    def mean(self, numbers: List[float]) -> float:
        return 10
    
def test_calculate():
    mock_request = MockRequest({"numbers": [ 10, 10]})
    calculator_4 = Calculator4(MockDriverHandler())

    response = calculator_4.calculate(mock_request)

    assert response == {'data': {'Calculator': 4, 'result': 10}}

def test_calculate_with_invalid_body():
    
    mock_request = MockRequest({"invalid_key": [1, 2, 3]})
    calculator_4 = Calculator4(MockDriverHandler())

    with raises(Exception) as excinfo:
        calculator_4.calculate(mock_request)

    assert "body mal formatado." in str(excinfo.value)