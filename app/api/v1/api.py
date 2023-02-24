from fastapi import APIRouter

from api.v1.endpoints import hello

api_router = APIRouter()

api_router.include_router(hello.router, prefix='/test', tags=['test', 'hello'])
