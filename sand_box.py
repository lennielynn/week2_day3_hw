
def grocery_quantities(grocery_list):
    # {'item': count}
    hash_map = {}
    for item in grocery_list:
        if item in hash_map:
            hash_map[item] += 1
        else:
            hash_map[item] = 1
    return hash_map
grocery_quantities(grocery_list)
# def grocery_quantities3(grocery_list):
#     # {'item': count}
#     hash_map = {}
#     for item in grocery_list:
#         hash_map[item] = hash_map.get(item, 0) + 1
#     return hash_map



# def grocery_quantities2(grocery_list):
#     # {'item': count}
#     hash_map = {}
#     for item in grocery_list:
#         if item not in hash_map:
#             hash_map[item] = 0
#         hash_map[item] += 1
#     return hash_map

 