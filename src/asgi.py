import logging

import uvicorn
from fastapi import Request, Response

from src.main import get_app
from src.utils import Timer

logger = logging.getLogger(__name__)

app = get_app()


@app.middleware("http")
async def middleware(request: Request, call_next: callable) -> Response:
    # record time taken for request
    with Timer() as timer:
        response = await call_next(request)

    request_path = request.scope["path"]
    request_method = request.scope["method"]
    logger.debug(f"t={timer.total_time}s [{request_method}] {request_path}")

    return response


if __name__ == "__main__":
    uvicorn.run(app, port=8080)
