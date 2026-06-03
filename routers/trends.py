from fastapi import APIRouter

from services.trend_service import get_trends

router = APIRouter()

#ML Kısmını üstlenen kişi oluşturacak
"""Bu modül proje mimarisi içerisinde
Makine Öğrenmesi ekibi tarafından geliştirilecek
Trend Tahmini ve Materyal Sınıflandırma modelleri ile
entegre olacak şekilde hazırlanacak

test amaçlı mock data kullandım"""


@router.get("/trends")
def trends():

    return {
        "trends": get_trends()
    }