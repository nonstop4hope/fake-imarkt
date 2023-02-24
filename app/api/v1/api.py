from fastapi import APIRouter

from api.v1.endpoints import hello, login, profile

api_router = APIRouter()

api_router.include_router(hello.router, prefix='/test', tags=['hello'])
api_router.include_router(login.router, prefix='/auth', tags=['login'])
api_router.include_router(profile.router, prefix='/profile', tags=['profile'])