# Define a function that takes a list of lists and returns a new list of
# lists with a student's name and their average grade in each sublist.

def average_grade(lst: list):
    """ Return students' names and their average grades.
    
    # >>> average_grade([['Bob', 56, 80, 72, 90], ['Alice', 60, 88, 44, 70]])
    # >>> [['Bob', 74.5], ['Alice', 65.5]]
    """
    for idx, small_list in enumerate(lst):
        average = 0
        # for index, x in enumerate(small_list[1:]):
        #     average += x
        # yield [lst[idx][0], average / (index + 1)]
        yield [lst[idx][0],sum(small_list[1:])/(len(small_list)-1)]
#TODO sum method - done

print(list(average_grade([['Bob', 56, 80, 72, 90], ['Alice', 60, 88, 44, 70]])))
