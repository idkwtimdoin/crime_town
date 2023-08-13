import logging

import uvicorn
from fastapi import Request, Response

from src.main import get_app
from src.utils import Timer

logger = logging.getLogger(__name__)

app, _ = get_app()


@app.middleware("http")
async def middleware(request: Request, call_next) -> Response:
    # record time taken for request
    with Timer() as timer:
        response = await call_next(request)

    host, port = request.scope["client"]
    request_path = request.scope["path"]
    request_method = request.scope["method"]
    logger.debug(f"{host}:{port} t={timer.total_time}s [{request_method}] {request_path}")

    return response


if __name__ == "__main__":
    uvicorn.run(app, port=8080)
