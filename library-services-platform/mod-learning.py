__version__ = "0.0.1"

from fastapi import FastAPI

intelligence  = FastAPI()

@app.get("/")
async def root():
    return { "msg": "FOLIO mod-learning", 
             "version": __version__ }