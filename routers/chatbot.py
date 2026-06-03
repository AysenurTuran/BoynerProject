"""Bu dosya chatbot endpointlerini içerir.

Yapılan Çalışmalar:
- Kullanıcı mesajlarının alınması
- Gemini servisinin çağrılması
- Yapay zeka cevaplarının API üzerinden döndürülmesi

Endpoint:
POST /chat"""

from fastapi import APIRouter

from schemas.chatbot import ChatRequest
from services.gemini_service import ask_gemini

router = APIRouter()


@router.post(
    "/chat",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    response = ask_gemini(
        request.message
    )

    return {
        "response": response
    }