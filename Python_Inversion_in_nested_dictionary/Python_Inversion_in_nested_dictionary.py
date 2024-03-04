# test_dict1 = {'a' : {'b' : {}}, 'd' : {'e' : {}}, 'f' : {'g' : {}}}
# test_dict2 = {'a' : {'b' : { 'c' : {}}}}


# finding the list of keys ~~~~~~~~~~~~~~~


def keys_finder(input_dict):
    list_of_keys = []
    temp_dict = input_dict

    for item in temp_dict.items():
        key, value = item

    while True:

        if value != {}:
            list_of_keys.append(key)
            temp_dict = value
            for item in temp_dict.items():
                key, value = item
        else:
            list_of_keys.append(key)
            break
    return list_of_keys


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def inverted_dict(input_dict):
    keys = keys_finder(input_dict)
    len_keys = len(keys)
    temp_dict = {}
    inverted = {}

    for i in range(len_keys):
        temp_dict[keys.pop(0)] = inverted
        inverted = temp_dict.copy()
        # print(inverted)
        temp_dict.clear()
    return inverted


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def main(input_dict):
    final_dict = {}
    list_of_items_in_input_dict = []
    print("old: ", input_dict)
    for key, value in input_dict.items():
        temp_dict = {}
        temp_dict[key] = value
        list_of_items_in_input_dict.append(temp_dict)

    for _dict in list_of_items_in_input_dict:
        result = inverted_dict(_dict)
        for key, value in result.items():
            final_dict[key] = value
    print("new: ", final_dict)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# running ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

test_dict1 = {"a": {"b": {}}, "d": {"e": {}}, "f": {"g": {}}}
test_dict2 = {"a": {"b": {"c": {}}}}

main(test_dict1)
main(test_dict2)
