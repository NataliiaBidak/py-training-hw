"""
Task 1
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line
"""
print("Task1")
[print(x, end=', ') for x in range(2000, 3201) if x % 7 == 0 and x % 5 != 0]
print([x for x in range(2000, 3201) if x % 7 == 0 and x % 5 != 0])

y = []
for x in range(2000, 3201):
    if x % 7 == 0 and x % 5 != 0:
        y.append(x)
print(y)

"""
Task 2
With a given integer number n, write a program to generate a dictionary that
contains (i, i*i) such that is an integer number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""
print("Task2")
b = int(input("Type some number:\n"))
a = {i: i * i for i in range(1, b + 1)}
print(a)
print(a[5])

"""
Task 3
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
"""
print("Task3")
n = input("Type some numbers:\n")
n = n.split(",")
b = []
for x in n:
    if x.isnumeric():
        b.append(x)
print([x for x in n if x.isnumeric()])
print(tuple(x for x in n if x.isnumeric()))
"""
Task 4
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
"""
print("Task4")
import math

a = input("Type some numbers:\n")
a = a.split(",")
c = 50
h = 30
a = [print(int(math.sqrt(2 * c * int(x) / h)), end=', ') for x in a if x.isnumeric()]
"""
Task 5
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
"""
print("\nTask5")
a = input("Type some numbers:\n")
i, j = str(a).split(",")
print(i, j)
matrix = [[int(x) * int(y) for x in range(int(j))] for y in range(int(i))]
print(matrix)
"""
Task 6
Write a program that accepts sequence of lines as input and prints the lines
after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
"""
print("Task6")
b = []
while True:
    a = input('Enter the line:\n')
    if a == '':
        break
    b.append(a.upper())
print('\n'.join(b))
"""
Task 7
Write a program that accepts a sequence of whitespace separated words as input
and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
"""
print("Task7")
a = input("Type some words:\n")
a = a.split(" ")
b = set(a)
a = list(b)
a.sort()
print(a)
"""
Task 8
Write a program which accepts a sequence of comma separated 4 digit binary
numbers as its input and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.
"""
print("Task8")
a = input("Type some digit binary numbers:\n")
a = a.split(",")
[print(x) for x in a if int(x, 2) % 5 == 0]
"""
Task 9
Write a program, which will find all such numbers between 1000 and 3000 (both included)
such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""
print("Task9")
print([x for x in range(1000, 3001) if len([c for c in str(x) if int(c) % 2 == 0]) == 4])
"""
Task 10
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
"""
print("Task10")
print("DIGITS: ", len([x for x in n if x.isnumeric()]))
print("LETTERS: ", len([x for x in n if x.isalpha()]))
"""
Task 11
Given a list of shuffled values.
Loop through it and find value 42.
If value was not found - print appropriate message.
Do not go through whole list - stop when succeeded.
some_list = list(range(100))
random.shuffle(some_list)
Example output (2 cases: was and was not found):
"Found 42! It took {attempts} attempt(s) before success."
"42 was not found"
"""
import random

some_list = list(range(100))
random.shuffle(some_list)

some_list.remove(42)

for x, idx in enumerate(some_list):
    if x == 42:
        print(f"Found 42! It took {idx} attempts before success")
        break
else:
    print("42 was not found")

# ======================================================================================


def func_name(a: int, b:str, *args, c: int = 42, **kwargs):
    """
    docstring
    :param a:
    :param b:
    :param args:
    :param c:
    :param kwargs:
    :return:
    """
    print(a, b)
    # print(args)
    print(c)

x = 3
y=4
# func_name(x, y)
func_name(1,2,3,4,5, d=42)





