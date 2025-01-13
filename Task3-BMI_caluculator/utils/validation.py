# utils/validation.py
def validate_input(value, min_val, max_val):
    try:
        val = float(value)
        if min_val <= val <= max_val:
            return val
        else:
            raise ValueError
    except ValueError:
        return None
