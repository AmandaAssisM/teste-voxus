from fastapi import FastAPI
from teste_pratico_voxus.routers import jokes_routers

app = FastAPI()

app.include_router(jokes_routers.router, prefix="/api/jokes", tags=["Piadas"])
