#!/usr/bin/python3

#def print_sorted_dictionary(a_dictionary):
#     num = 0
#     new_dict = {}
#     temp = list(map(lambda x: str(a_dictionary[x]), a_dictionary))
#     temp.sort()
#     while num < len(a_dictionary):
#         for i, v in a_dictionary.items():
#             if str(v) == temp[num]:
#                 new_dict[i] = v
#         num += 1
#     print(new_dict)
#alternatively

# def print_sorted_dictionary(a_dictionary):
#     sort = dict(sorted(a_dictionary.items(), key=lambda item: str(item[1])))
#     for key, value in sort.items():
#         print(f"{key}: {value}")

def print_sorted_dictionary(a_dictionary):
    for llave in sorted(a_dictionary):
        print("{}: {}".format(llave, a_dictionary[llave]))
