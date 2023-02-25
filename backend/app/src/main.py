import logging
import pathlib

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.v1.api import api_router
from app.config import settings


logger = logging.getLogger(__name__)

app = FastAPI(title=settings.PROJECT_NAME)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )


app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == '__main__':
    cwd = pathlib.Path(__file__).parent.resolve()
    uvicorn.run(app, host=settings.SERVER_HOST, port=settings.SERVER_PORT, log_config=f'{cwd}/loging.ini')
