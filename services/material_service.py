def get_material_suggestions(material: str):

    # ML Kısmını üstlenen kişi oluşturacak
    """Bu modül proje mimarisi içerisinde
    Makine Öğrenmesi ekibi tarafından geliştirilecek
    Trend Tahmini ve Materyal Sınıflandırma modelleri ile
    entegre olacak şekilde hazırlanacak

    test amaçlı mock data kullandım"""

    suggestions = {
        "denim": [
            "Laptop Çantası",
            "Tote Bag",
            "Cüzdan"
        ],
        "pamuk": [
            "Bez Çanta",
            "Mutfak Önlüğü",
            "Yastık Kılıfı"
        ],
        "polyester": [
            "Spor Çantası",
            "Kozmetik Çantası"
        ]
    }

    return suggestions.get(
        material.lower(),
        ["Bez Çanta"]
    )