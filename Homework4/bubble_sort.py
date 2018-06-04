# Use bubble sort to solve this problem.
# Wiki on the algorithm at https://en.wikipedia.org/wiki/Bubble_sort


def bubble_sort(numbers: list):
    """ Use bubble sort to sort a list of numbers in ascending order.
        Return the input list after mutating it with sorted numbers.
    
    # >>> bubble_sort([2, 19, 4, 1, -40])
    [-40, 1, 2, 4, 19]
    # >>>
    """

    # your code here
    for idx in range(len(numbers)-1):

        for ind, number in enumerate(numbers[:-1]):
            if numbers[ind] < numbers[ind+1]:
                numbers[ind], numbers[ind+1] = numbers[ind+1], numbers[ind]

        print(numbers)
    return numbers


print(list(bubble_sort([2, 19, 4, 1, -40])))
