import logging

from fastapi import APIRouter, Depends

from schemas.user import User
from src.jwt_auth import get_current_active_user

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get('/me', response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user
