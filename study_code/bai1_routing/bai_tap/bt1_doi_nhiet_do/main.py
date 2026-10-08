from fastapi import HTTPException
from enum import Enum
from fastapi import FastAPI

app = FastAPI()

class Unit(str, Enum):
    C = 'celsius'
    F = 'fahrenheit'
    K = "kelvin"

@app.get('/convert/{unit}')
def convert(unit: Unit, value: float, to: Unit):
    if unit == to:
        raise HTTPException(status_code = 400, detail = 'Not convert to same unit')
    if (unit == Unit.C and value < -273.15) or (unit == Unit.K and value < 0) or (unit == Unit.F and value < -459.67):
        raise HTTPException(status_code = 400, detail = 'Temperature cannot be below absolute zero')
    if unit == Unit.C:
        if to == Unit.F:
            return {'from': unit, 'to': to, 'input': value, 'result': round((9/5) * value + 32,2)}
        elif to == Unit.K:
            return {'from': unit, 'to': to, 'input': value, 'result': round(value + 273.15, 2)}
    elif unit == Unit.F:
        if to == Unit.C:
            return {'from': unit, 'to': to, 'input': value, 'result': round((5/9) * (value - 32),2)}
        elif to == Unit.K:
            return {'from': unit, 'to': to, 'input': value, 'result': round((5/9) * (value - 32) + 273.15,2)}
    elif unit == Unit.K:
        if to == Unit.C:
            return {'from': unit, 'to': to, 'input': value, 'result': round(value - 273.15,2)}
        elif to == Unit.F:
            return {'from': unit, 'to': to, 'input': value, 'result': round((9/5) * (value - 273.15) + 32,2)}

