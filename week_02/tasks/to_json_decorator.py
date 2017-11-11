import functools


def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        return {"{}".format(func.__name__): result}
    return wrapped


@to_json
def summator(num_list):
    return sum(num_list)


@to_json
def squarefy(number: int):
    return number * number

print(summator([1, 2, 3, 4, 5]))
print(squarefy(4))
