

# for checking query params validation
def is_valid_dict(dictionary, key_tuple):
    invalid_key = None
    for key in dictionary:
        if key not in key_tuple:
            invalid_key = key
            break
    return invalid_key is None, invalid_key
