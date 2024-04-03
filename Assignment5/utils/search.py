def myFilter(values, condition):
    result = []
    for value in values:
        if condition(value):
            result.append(value)
    return result