from typing import Tuple
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi_versioning import VersionedFastAPI
from starlette.staticfiles import StaticFiles
from pathlib import Path


from src.api import v1_router

APP_TITLE = "CIA app"
OPENAPI_URL = "/openapi.json"
SWAGGER_UI_OAUTH_2_REDIRECT_URL = "/docs/oauth2-redirect"


def get_app() -> Tuple[FastAPI, FastAPI]:
    app = FastAPI(
        title=APP_TITLE,
        docs_url=None,
        redoc_url=None,
        openapi_url=OPENAPI_URL,
        swagger_ui_oauth2_redirect_url=SWAGGER_UI_OAUTH_2_REDIRECT_URL,
    )
    app.include_router(v1_router)
    v1_app = VersionedFastAPI(
        app,
        version_format="{major}",
        prefix_format="/v{major}",
        docs_url=None,
        redoc_url=None,
        openapi_url=OPENAPI_URL,
        swagger_ui_oauth2_redirect_url=SWAGGER_UI_OAUTH_2_REDIRECT_URL,
    )
    v1_app.mount(
        path="/static",
        app=StaticFiles(directory="src/static"),
        name="static",
    )

    # * homepage
    @v1_app.get("/", response_class=HTMLResponse)
    async def home():
        content = Path("src/static/index.html").read_text()
        return content

    return v1_app, app
