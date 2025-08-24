from fastapi import APIRouter, Cookie

router = APIRouter()

@router.get("/cookie")
def get_cookies(ga: str = Cookie(None)):
    return {"ga": ga}