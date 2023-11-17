from pathlib import Path

import uvicorn as uvicorn
from fastapi import FastAPI
from starlette.responses import FileResponse
from starlette.routing import Route


path = Path("ssiptv.iptv.online.m3u")


def download_file(*args, **kwargs):
    return FileResponse(path=str(path), filename=path.name, media_type='multipart/form-data')


routes = [Route("/iptv", endpoint=download_file, methods=["GET"])]
app = FastAPI(routes=routes)


if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, reload=False, log_level="info")
