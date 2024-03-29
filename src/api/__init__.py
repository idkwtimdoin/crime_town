from fastapi import APIRouter
from fastapi_versioning import versioned_api_route

from src.api.crime import router as crime_router

router = APIRouter(route_class=versioned_api_route(1))
router.include_router(crime_router)
