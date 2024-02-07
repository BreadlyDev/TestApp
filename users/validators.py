def validate_phone(phone):
    return phone.isdigit()


def validate_class(_class):
    return _class[1:] == '[]'
