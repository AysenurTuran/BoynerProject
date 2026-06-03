from fastapi import APIRouter

from schemas.material import MaterialRequest
from services.material_service import get_material_suggestions


#ML Kısmını üstlenen kişi oluşturacak
"""Bu modül proje mimarisi içerisinde
Makine Öğrenmesi ekibi tarafından geliştirilecek
Trend Tahmini ve Materyal Sınıflandırma modelleri ile
entegre olacak şekilde hazırlanacak

test amaçlı mock data kullandım"""

router = APIRouter()


@router.post("/material-suggestion")
def material_suggestion(
        request: MaterialRequest
):

    return {
        "material": request.material,
        "suggestions":
            get_material_suggestions(
                request.material
            )
    }