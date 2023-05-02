# Raises an error if the given parameter is lower or equal to zero.
def is_positive(number):
    if(number <= 0):
        raise InvalidValue("The numerical field must be a positive number.")

class InvalidValue(Exception):
    pass

