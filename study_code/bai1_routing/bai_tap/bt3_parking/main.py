from pydantic import BaseModel
from starlette.status import HTTP_404_NOT_FOUND
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from fastapi import HTTPException, FastAPI

app = FastAPI()

class Vehicles(BaseModel):
    bien_so: str

parking_lot = []

@app.get('/xe/dang-do')
def get_vehicles_park():
    return parking_lot

@app.post('/xe/vao', status_code=HTTP_201_CREATED)
def add_park(vehicles: Vehicles):
    if vehicles.bien_so in parking_lot:
        raise HTTPException(status_code=409, detail="This vehicles already exists")
    if len(parking_lot) == 5:
        raise HTTPException(status_code=409, detail ='The park is full')
    parking_lot.append(vehicles.bien_so)
    return {'bien_so': vehicles.bien_so}

@app.get('/trang-thai')
def get_trang_thai():
    return {'suc_chua': 5, 'dang_do': len(parking_lot), 'con_trong': 5 - len(parking_lot)}

@app.get('/xe/{bien_so}')
def get_vehicles_park_by_license_plate(bien_so: str):
    if bien_so not in parking_lot:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail = 'Not found this vehicles')
    return {'bien_so': bien_so}

@app.delete('/xe/ra/{bien_so}', status_code=HTTP_204_NO_CONTENT)
def delete_park(bien_so: str):
    if bien_so not in parking_lot:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail = 'Not found this vehicles')
    parking_lot.remove(bien_so)

