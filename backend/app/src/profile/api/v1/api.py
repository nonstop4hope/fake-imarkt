from fastapi import APIRouter

from app.api.v1.endpoints import hello
from app.api.v1.endpoints import profile, login

api_router = APIRouter()

api_router.include_router(hello.router, prefix='/test', tags=['hello'])
api_router.include_router(login.router, prefix='/auth', tags=['login'])
api_router.include_router(profile.router, prefix='/profile', tags=['profile'])