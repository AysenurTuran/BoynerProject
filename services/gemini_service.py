"""Bu servis Google Gemini API ile iletişim kurar.

Yapılan Çalışmalar:
- Gemini API bağlantısının kurulması
- Yapay zeka istemlerinin (prompt) hazırlanması
- Kullanıcı mesajlarının işlenmesi
- AI mentor chatbot cevaplarının üretilmesi

Bu modül proje kapsamında geliştirilen
AI Mentor Chatbot sisteminin çekirdeğini oluşturur"""

import google.generativeai as genai

from core.config import settings

genai.configure(
    api_key=settings.GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def ask_gemini(message: str):

    prompt = f"""
    Sen HERCYCLE AI adlı sistemin yapay zeka mentorusun.

    Amaçların:

    - Kadın girişimcilere destek olmak
    - Sürdürülebilir moda konusunda yardımcı olmak
    - Tekstil atıklarının değerlendirilmesini önermek
    - Üretim tavsiyeleri vermek
    - Trend önerileri sunmak

    Kullanıcı Mesajı:

    {message}
    """

    response = model.generate_content(prompt)

    return response.text