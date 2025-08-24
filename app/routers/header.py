from fastapi import APIRouter, Header

router = APIRouter()

@router.get("/header")
def get_headers(x_token: str = Header(None, title="토큰")):
    return {"X-Token": x_token}