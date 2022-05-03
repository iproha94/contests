a1 = {
    'b': 4,
    'c': {
        'd': 3,
        'e': 5,
    }
}

r = [
    ('b', 4),
    ('c.d', 3),
    ('c.e', 5),
]

a2 = {
    'b': 4,
    'c': {
        'd': {
            'f': {
                'h': 7,
            },
            'g': 6,
        },
        'e': 5,
    }
}


def rf(item, now_key, result):
    if isinstance(item, int):
        result.append((now_key, item))
        return

    for key in item.keys():
        rf(item[key], now_key + f".{key}" if now_key else f"{key}", result)


def f(tree):
    result = []
    rf(tree, f"", result)
    return result

print(f(a2))
