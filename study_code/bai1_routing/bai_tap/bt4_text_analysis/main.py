from pydantic import BaseModel
from typing import Annotated
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from fastapi import FastAPI, HTTPException, Query

app = FastAPI()

class Text(BaseModel):
    text_content: str
    

@app.post('/phan-tich', status_code=HTTP_201_CREATED)
def post_text(text: Text, top: Annotated[int, Query(ge = 1, le = 20)] = 5, bo_qua_so: bool = False):
    if text.text_content.strip() == '':
        raise HTTPException(status_code = HTTP_400_BAD_REQUEST, detail = {'error': 'Text cannot be empty or contain only whitespace'})
    word_split = text.text_content.split()
    if bo_qua_so:
        word_split = [w for w in word_split if not w.isdigit()]
    word_split = [w.lower() for w in word_split]
    dict_word = {}
    for word in word_split:
        if word in dict_word:
            dict_word[word] += 1
        else:
            dict_word[word] = 1
    dict_word = dict(sorted(dict_word.items(), key = lambda x: x[1], reverse = True)[:top])
    return {'character': len(text.text_content), 'word': len(word_split), 'top_of_word': dict_word}