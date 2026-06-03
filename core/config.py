"""Bu modül uygulama yapılandırmalarını yönetir.

Yapılan Çalışmalar:
- Environment değişkenlerinin okunması
- Gemini API anahtarının yönetimi
- Merkezi konfigürasyon yapısının oluşturulması"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    GEMINI_API_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()