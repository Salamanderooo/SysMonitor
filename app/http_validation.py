
def validate_status_code(expected_status_code):
    if not expected_status_code.isdigit():
        raise ValueError("The expected status code must be a number in the range 100-599.")        
    if not 100 <= int(expected_status_code) <= 599:
        raise ValueError("The expected status code must be a number in the range 100-599.")
    return int(expected_status_code)


validate_status_code("+400")
print(validate_status_code("+400"))  # Example usage