#1
def flatten_dict(my_dict):
    flat_dict = dict()
    for key, value in my_dict.items():
        if isinstance(my_dict[key], dict):
            for key1, value1 in my_dict[key].items():
                nest_key = f'{key}.{key1}'
                flat_dict[nest_key] = value1
        else:        
            flat_dict[key] = value
    return flat_dict
print(flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}))

#2
def unflatten_dict(my_dict2):
    unflat_dict = dict()
    for key, value in my_dict2.items():
        split_keys = key.split('.')
        if len(split_keys) > 1:
            outer_key = split_keys[0]
            inner_key = split_keys[1]

            if outer_key in unflat_dict:
                inner_dict = unflat_dict[outer_key]  # Corrected line
                inner_dict[inner_key] = value
            else:
                unflat_dict[outer_key] = {inner_key: value}  # Corrected line
        else:
            unflat_dict[key] = value
    return unflat_dict

print(unflatten_dict({'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}))


