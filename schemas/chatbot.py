"""Bu dosya chatbot API'sinde kullanılan
istek ve cevap modellerini tanımlar.

Yapılan Çalışmalar:
- Request modelleri
- Response modelleri
- Veri doğrulama yapıları"""

from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str