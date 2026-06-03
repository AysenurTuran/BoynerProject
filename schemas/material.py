#ML Kısmını üstlenen kişi oluşturacak
from pydantic import BaseModel


class MaterialRequest(BaseModel):
    material: str