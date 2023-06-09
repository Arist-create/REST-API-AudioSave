from fastapi import FastAPI
from src.database.main import init_db
from src.routers import add_audio_router, create_user_router, get_audio_router

app = FastAPI() 



@app.on_event("startup")
async def on_startup() -> None:
    await init_db()




app.include_router(add_audio_router.router)
app.include_router(create_user_router.router)
app.include_router(get_audio_router.router)
