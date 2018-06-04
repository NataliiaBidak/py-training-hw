"""
Flattens a nested dictionary by joining the keys with "." character.

    # >>> flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
    # >>> {'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}

"""


def flatten_dict(nested_dict, flattened=None):
    """
    Flattens a nested dict by joining the keys with "." character.

      # >>> flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
      # >>> {'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}
    """
    if flattened is None:
        flattened = dict()

    for key, value in nested_dict.items():
        if isinstance(value, dict):
            nested_dict.update(key + "." + list(value.keys())[1])
            flatten_dict(value, flattened=flattened)
        else:
            flattened.update({key: value})

    return flattened


if __name__ == '__main__':
    print(flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}))
    # index = None
    #             for ind,elem in enumerate(nested_dict.keys()):
    # if elem ==key:
    #     index = ind
    # flattened.update({(list(nested_dict.keys())[ind]+"."+key):value})
