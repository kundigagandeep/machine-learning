import dl_translate as dlt
from fastapi import FastAPI

mt = dlt.TranslationModel("facebook/m2m100_418M") 

app = FastAPI()

@app.get('/')
async def translate_en_pl(text: str, source_lang:str, target_lang: str):

    return mt.translate(text, source=source_lang , target=target_lang)