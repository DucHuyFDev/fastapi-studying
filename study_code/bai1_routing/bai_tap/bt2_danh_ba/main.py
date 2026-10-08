from starlette.status import HTTP_404_NOT_FOUND
from fastapi import HTTPException
from pydantic import BaseModel
from starlette.status import HTTP_201_CREATED
from fastapi import FastAPI

app = FastAPI()

class Contact(BaseModel):
    name: str
    phone: str

contacts: dict[int, dict] = {
    1: {'name': 'Nguyen Van A', 'phone': '0123654987'},
    2: {'name': 'Tran Thi B', 'phone': '0987654321'},
    3: {'name': 'Duong Ha C', 'phone': '0548796321'}
}

@app.post('/contacts', status_code=HTTP_201_CREATED)
def create_contact(new_contact: Contact):
    if new_contact.phone in [c['phone'] for c in contacts.values()]:
        raise HTTPException(status_code=409, detail='This phone number is exists')
    id = max(contacts, default=0) + 1
    contacts[id] = new_contact.model_dump()
    return {'id': id, **contacts[id]}

@app.get('/contacts')
def get_contact(q: str, limit: int= 10):
    return [c for c in contacts.values() if q.lower() in c['name'].lower()][:limit]

@app.get('/contacts/{id}')
def get_contact_by_id(id: int):
    if id not in contacts:
        raise HTTPException(status_code=404, detail='Not found this contact')
    return {'id': id, **contacts[id]}

@app.put('/contacts/{id}')
def update_contact_by_id(id: int, contact: Contact):
    if id not in contacts:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail='Not found this contact')
    contacts[id] = contact.model_dump()
    return {'id': id, **contacts[id]}

@app.delete('/contacts/{id}', status_code=204)
def delete_contact_by_id(id: int):
    if id not in contacts:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail='Not found this contact')
    del contacts[id]

    
