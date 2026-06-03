"""
- FastAPI uygulamasının oluşturulması
- Router yönetimi
- API endpointlerinin sisteme dahil edilmesi
- Swagger dokümantasyonunun oluşturulması
"""

from fastapi import FastAPI

from routers import (
    chatbot,
    materials,
    trends,
    health
)

app = FastAPI(
    title="HERCYCLE AI Backend",
    version="1.0.0"
)

app.include_router(
    chatbot.router,
    tags=["Chatbot"]
)

app.include_router(
    materials.router,
    tags=["Materials"]
)

app.include_router(
    trends.router,
    tags=["Trends"]
)

app.include_router(
    health.router,
    tags=["Health"]
)