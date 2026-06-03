""""Bu endpoint backend servisinin çalışır
durumda olup olmadığını kontrol etmek için geliştirilmiştir.

Endpoint:
GET /health"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health():

    return {
        "status": "running"
    }