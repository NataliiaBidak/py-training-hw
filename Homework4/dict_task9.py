"""
Write a Python program to convert list to list of dictionaries.
Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]

"""


def convert_list(lst: list):
    d = {}
    final_list = []
    # for index, element in enumerate(range(len(lst[0]))):
    #     d["color_name"] = lst[0][index]
    #     d["color_code"] = lst[1][index]
    #     final_list.append(d)
    # return final_list

    color_tuple = zip(lst[0], lst[1])
    return [{"color_name": x, "color_code": y} for x, y in color_tuple]

    # for x, y in color_tuple:
    #     d["color_name"] = x
    #     d["color_code"] = y
    #     final_list.append(d)
    # return final_list


# print(convert_list([["Black", "Red", "Maroon", "Yellow"]]))
print(convert_list([["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]]))
