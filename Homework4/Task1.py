'''
implement function my_map that would work as built-in map function
'''
# print(list(map(lambda x: x > 5, range(10))))

def my_map(func: callable, list_of_el: list):
    # for x in list_of_el:
    #     yield func(x)

    return [func(x) for x in list_of_el]

#TODO list comprehention - done


print(list(my_map(lambda x: x > 5, range(10))))
print(list(my_map(lambda x: x > 6, range(10))))
