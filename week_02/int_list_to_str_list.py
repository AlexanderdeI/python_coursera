def to_str_list(iterable):
    """Convert to string"""
    return list(map(str, iterable))

int_list = [1, 2, 3, 4, 5]
print(to_str_list(int_list))