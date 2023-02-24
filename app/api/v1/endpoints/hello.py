import logging
from typing import Any

from fastapi import APIRouter
from starlette import status

from schemas.hello_response import HelloResponse

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get('/hello', response_model=HelloResponse, status_code=status.HTTP_200_OK)
async def hello() -> Any:
    return HelloResponse(hello='World')
