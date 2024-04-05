```markdown
# Custom Calculator API

This FastAPI application serves as a custom calculator, offering various endpoints for performing arithmetic operations, conversions, and checks.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Cozyamy/hackathon/Custom_Calculator_API.git
   ```

2. Install dependencies:
   ```bash
   poetry shell
   poetry install
   ```

## Usage

1. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

2. The API will be available at `http://localhost:8000`.

## Endpoints

### POST /calculate

Perform arithmetic operations based on the provided operation and operands.

- **Request Body**: Accepts an `ArithmeticOperation` model containing the operation type (`operation`) and two operands (`operand1`, `operand2`).
- **Response Body**: Returns the result of the arithmetic operation as a float.

### GET /convert/temperature

Convert temperature between different units.

- **Query Parameters**:
  - `from_unit` (str): The unit to convert from. Choices: "Celsius", "Fahrenheit", "Kelvin".
  - `to_unit` (str): The unit to convert to.
  - `value` (float): The temperature value to convert.
- **Response Body**: Returns the converted temperature value as a float.

### GET /factorial

Calculate the factorial of a number.

- **Query Parameter**:
  - `n` (int): The number for which to calculate the factorial. Must be between 0 and 20.
- **Response Body**: Returns the factorial of the number as an integer.

### GET /interest

Calculate simple interest.

- **Query Parameters**:
  - `principal` (float): The principal amount.
  - `rate` (float): The interest rate.
  - `time` (int): The time period in years.
- **Response Body**: Returns the calculated simple interest as a float.

### GET /palindrome

Check if a string is a palindrome.

- **Query Parameter**:
  - `text` (str): The string to check for palindrome.
- **Response Body**: Returns a boolean indicating whether the string is a palindrome.

## Models

### ArithmeticOperation

Represents an arithmetic operation request.

```python
class ArithmeticOperation(BaseModel):
    operation: str
    operand1: float
    operand2: float
```

### TemperatureConversion

Represents a temperature conversion request.

```python
class TemperatureConversion(BaseModel):
    from_unit: str
    to_unit: str
    value: float
```

### FactorialQuery

Represents a factorial calculation request.

```python
class FactorialQuery(BaseModel):
    n: int
```

### InterestQuery

Represents an interest calculation request.

```python
class InterestQuery(BaseModel):
    principal: float
    rate: float
    time: int
```

### PalindromeQuery

Represents a palindrome check request.

```python
class PalindromeQuery(BaseModel):
    text: str
```
```