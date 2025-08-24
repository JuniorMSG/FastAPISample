from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates

error_router = APIRouter()
templates = Jinja2Templates(directory="templates")

# exception handler는 main.py에서 처리하도록 함수만 정의
async def http_exception_handler(request: Request, exc: HTTPException):
    return templates.TemplateResponse(
        "errors/error.html",
        {"request": request, "status_code": exc.status_code, "detail": exc.detail},
        status_code=exc.status_code
    )
