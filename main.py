
from fastapi import FastAPI
from be_task_ca.user_clean.interface.router import router as user_router
from be_task_ca.item_clean.interface.router import router as item_router

app = FastAPI()
app.include_router(user_router, prefix="/api")
app.include_router(item_router, prefix="/api")
