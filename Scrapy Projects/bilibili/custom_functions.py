# extract all values corresponding to a key regardless of depth of nestings.
def dict_find_all(key, value):
    for k, v in (value.items() if isinstance(value, dict) else
                 enumerate(value) if isinstance(value, list) else []):
        if k == key:
            yield v
        elif isinstance(v, (dict, list)):
            yield from dict_find_all(key, v)