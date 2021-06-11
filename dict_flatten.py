def flatten_dict(dict_obj):
    temp_dict = {}
    for key, value in dict_obj.items():
        if isinstance(value, dict):
            temp_dict.update(flatten_dict(create_new_dict(value, key)))
        elif isinstance(value, list):
            for i in range(len(value)):
                temp_dict.update(flatten_dict(create_new_dict(value[i], key + "[{}]".format(i))))
        else:
            temp_dict[key] = value
    return temp_dict

def create_new_dict(dict_obj, prefix = None):
    prefix = prefix or ""
    return {prefix + "." + key: value for key, value in dict_obj.items()}