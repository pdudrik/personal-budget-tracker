from .models import ExpenseCategory


def valid_int_id(value):
    try:
        num = int(value)
    except (ValueError, TypeError):
        return None
    
    if num > 0:
        return num
    return None


def get_categories_json():
    data = {}
    for category in ExpenseCategory.objects.prefetch_related("subcategories").all():
        data[str(category.id)] = []
        
        for subcategory in category.subcategories.all():
            data[str(category.id)].append({
                "id": str(subcategory.id),
                "name": subcategory.name,
            })
    
    return data