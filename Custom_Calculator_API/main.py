from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import math

app = FastAPI()

class ArithmeticOperation(BaseModel):
    operation: str
    operand1: float
    operand2: float

class TemperatureConversion(BaseModel):
    from_unit: str
    to_unit: str
    value: float

class FactorialQuery(BaseModel):
    n: int

class InterestQuery(BaseModel):
    principal: float
    rate: float
    time: int

class PalindromeQuery(BaseModel):
    text: str

@app.post("/calculate", response_model=float)
def calculate_arithmetic(operation_data: ArithmeticOperation):
    """
    Perform arithmetic operations based on the provided operation and operands.

    Args:
        operation_data (ArithmeticOperation): The arithmetic operation request.

    Returns:
        float: The result of the arithmetic operation.
    """
    if operation_data.operation == "add":
        return operation_data.operand1 + operation_data.operand2
    elif operation_data.operation == "subtract":
        return operation_data.operand1 - operation_data.operand2
    elif operation_data.operation == "multiply":
        return operation_data.operand1 * operation_data.operand2
    elif operation_data.operation == "divide":
        if operation_data.operand2 == 0:
            raise HTTPException(status_code=400, detail="Division by zero is not allowed")
        return operation_data.operand1 / operation_data.operand2
    else:
        raise HTTPException(status_code=400, detail="Invalid operation")

@app.get("/convert/temperature", response_model=float)
def convert_temperature(from_unit: str = Query(..., choices=["Celsius", "Fahrenheit", "Kelvin"]),
                        to_unit: str = Query(...),
                        value: float = Query(...)):
    """
    Convert temperature between different units.

    Args:
        from_unit (str): The unit to convert from.
        to_unit (str): The unit to convert to.
        value (float): The temperature value to convert.

    Returns:
        float: The converted temperature value.
    """
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        raise HTTPException(status_code=400, detail="Invalid temperature conversion")

@app.get("/factorial", response_model=int)
def calculate_factorial(n: int = Query(..., title="Number of Factorial", ge=0, le=20)):
    """
    Calculate the factorial of a number.

    Args:
        n (int): The number for which to calculate the factorial.

    Returns:
        int: The factorial of the number.
    """
    return math.factorial(n)

@app.get("/interest", response_model=float)
def calculate_interest(principal: float = Query(..., title="Principal Amount"),
                       rate: float = Query(..., title="Interest Rate"),
                       time: int = Query(..., title="Time in Years", gt=0)):
    """
    Calculate simple interest.

    Args:
        principal (float): The principal amount.
        rate (float): The interest rate.
        time (int): The time period in years.

    Returns:
        float: The calculated simple interest.
    """
    return (principal * rate * time) / 100

@app.get("/palindrome", response_model=bool)
def check_palindrome(text: str = Query(...)):
    """
    Check if a string is a palindrome.

    Args:
        text (str): The string to check for palindrome.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    return text == text[::-1]