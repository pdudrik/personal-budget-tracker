
def valid_int_id(value):
    try:
        num = int(value)
    except (ValueError, TypeError):
        return None
    
    if num > 0:
        return num
    return None