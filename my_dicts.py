def add_element(d, key, value):
    d[key] = value
    return d


def remove_element(d, key):
    d.pop(key, None)
    return d


def merge_dicts(d1, d2):
    return {**d1, **d2}


def find_by_key(d, key):
    return d.get(key)


def get_all_keys(d):
    return list(d.keys())


def get_all_values(d):
    return list(d.values())
