from fastapi import FastAPI, Request
from fastapi.routing import APIRoute, APIRouter
from fastapi_versioning import VersionedFastAPI

from src.utils import Stopwatch


APP = FastAPI()
API_VERSIONS = ["v0", "v1"]


async def middleware(request: Request, call_next):
    with Stopwatch() as sw:
        response = await call_next(request)
    return response

versioned_routers = []
for version in API_VERSIONS:
    router = APIRouter(route_class=APIRoute)
    versioned_routers.append((router, f"/{version}"))

app = VersionedFastAPI(
    APP, routes=versioned_routers, middleware=[middleware]
)
