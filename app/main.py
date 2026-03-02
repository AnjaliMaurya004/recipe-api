from fastapi import Depends, FastAPI
from app import models
from app.routers import recipe, users, auth
from fastapi.staticfiles import StaticFiles

models.Base.metadata.create_all(bind=models.engine)
app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(recipe.router)
app.include_router(users.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

