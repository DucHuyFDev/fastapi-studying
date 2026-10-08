from enum import Enum
from typing import Annotated

from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel

# Nguyên tắc khai báo thứ tự API: Route cố định khai báo trước, route parameter khai báo sau cùng

app = FastAPI(title = 'Coffee Store')

menu: dict[int, dict] = {
    1: {'name': 'Milk coffee', 'price': 25000},
    2: {'name': 'Watermelon juice', 'price': 45000},
    3: {'name': 'Orange juice', 'price': 50000}
}

class Size(str, Enum):
    S = 'S'
    M = 'M'
    L = 'L'

class NewItem(BaseModel):
    name: str
    price: int

@app.get('/')
def root():
    return {'message': 'Welcome to coffee store !'}

@app.get('/menu')
def list_menu(
    keyword: Annotated[str | None, Query(min_length=2, max_length=30)] = None,
    max_price: int | None = None
):
    # Keyword is a parameter (parameter query)
    # Min_length and max_length are constraint for the parameter
    items = [{'id': i, **d} for i, d in menu.items()]
    if keyword:
        items = [x for x in items if keyword.lower() in x['name'].lower()]
    if max_price is not None:
        items = [x for x in items if x['price'] <= max_price]
    return items

@app.get('/menu/{item_id}')
def get_item(item_id: int):
    if item_id not in menu:
        raise HTTPException(status_code = 404, detail = 'Cannot find this taste')
    return {'id': item_id, **menu[item_id]}

@app.get('/size/{size}')
def size_info(size: Size):
    extra = {Size.S: 0, Size.M: 5000, Size.L: 10000}
    return {'size': size, 'phu_thu': extra[size]}

@app.post('/menu', status_code = status.HTTP_201_CREATED)
def create_item(item: NewItem):
    new_id = max(menu, default = 0) + 1 # lấy key lớn nhất và +1 cho sản phẩm mới, mặc định là 0 nếu menu rỗng
    menu[new_id] = item.model_dump() # chuyển đổi data từ dạng Pydantic model thành dictionary
    return {'id': new_id, **menu[new_id]}

@app.put('/menu/{item_id}')
def replace_item(item_id: int, item: NewItem):
    if item_id not in menu:
        raise HTTPException(status_code = 404, detail = 'Not found this taste')
    menu[item_id] = item.model_dump()
    return {'id': item_id, **menu[item_id]}

@app.delete('/menu/{item_id}', status_code = status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    if item_id not in menu:
        raise HTTPException(status_code = 404, detail = 'Not found this taste')
    del menu[item_id]    