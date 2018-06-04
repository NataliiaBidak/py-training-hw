"""
1.  Write a Python program to read an entire text file.
2.  Write a Python program to read first n lines of a file.
3.  Write a Python program to append text to a file and display the text.
4.  Write a Python program to read last n lines of a file.
5.  Write a Python program to read a file line by line and store it into a list.
6.  Write a Python program to read a file line by line store it into a variable.
7.  Write a Python program to read a file line by line store it into an array.
8.  Write a python program to find the longest words.
9.  Write a Python program to count the number of lines in a text file.
10. Write a Python program to count the frequency of words in a file.
11. Write a Python program to get the file size of a plain file.
12. Write a Python program to write a list to a file.
13. Write a Python program to copy the contents of a file to another file .
14. Write a Python program to combine each line from first file with the corresponding line in second file.
15. Write a Python program to read a random line from a file.
16. Write a Python program to assess if a file is closed or not.
17. Write a Python program to remove newline characters from a file.
"""
import os
import random

print("Task1 -  Write a Python program to read an entire text file. ")
with open("file_for_task14", 'r') as file:
    print(file.read())

print("Task2 -  Write a Python program to read first n lines of a file. ")
with open("file_for_task14", 'r') as file:
    for x in file.readlines()[:4]:
        print(x)

print("Task3 - Write a Python program to append text to a file and display the text.")
with open("file_for_task14", 'a+') as file:
    file.write("\nLast added line for task 3")
file = open("file_for_task14", 'r')
print(file.read())
file.close()

print("Task4 - Write a Python program to read last n lines of a file.")
with open("file_for_task14", 'r') as file:
    for x in file.readlines()[9:]:
        print(x)

print("Task5 -  Write a Python program to read a file line by line and store it into a list.")
with open("file_for_task14", 'r') as file:
    list_of_lines = []
    for x in file.readlines():
        list_of_lines.append(x)
    print(list_of_lines)

print("Task6 -  Write a Python program to read a file line by line store it into a variable.")
with open("file_for_task14", 'r') as file:
    store = ""
    for x in file.readlines():
        store += x
    print(store)

print("Write a python program to find the longest words. ")
with open("file_for_task14", 'r') as file:
    stored_file = file.read()
    list_of_words = stored_file.split()
    length = 0
    for idx, x in enumerate(list_of_words):
        length_of_word = len(list_of_words[idx])
        if length_of_word > length:
            length = length_of_word
    print(length)
print("9.  Write a Python program to count the number of lines in a text file.")
with open("file_for_task14", 'r') as file:
    counter = 0
    for x in file.readlines():
        counter += 1
    print(counter)
print("10. Write a Python program to count the frequency of words in a file.")
with open("file_for_task14", 'r') as file:
    counter = 0
    for line in file.readlines():
        counter += line.count("you")
    print(counter)
print("11. Write a Python program to get the file size of a plain file.")
print(os.stat("file_for_task14").st_size)

print("12. Write a Python program to write a list to a file.")
with open("file_for_task14", 'a+') as file:
    list_of_ford_cars = ["Falcon", "Focus", "Festiva", "Fairlane"]
    for car in list_of_ford_cars:
        file.write("\n" + car)

print(" Write a Python program to copy the contents of a file to another file .")
with open("file_for_task14", 'r') as file:
    second_file = open("file_for_subtask_13", 'w')
    for line in file.readlines():
        second_file.write(line)
    second_file.close()

print("14. Write a Python program to combine each line from first file with the corresponding line in second file.")
with open("file_for_task14", 'r') as file:
    with open("file_for_subtask_13", 'r') as second_file:
        combined_list = list(zip(file.readlines(), second_file.readlines()))
    print(combined_list)

print("15. Write a Python program to read a random line from a file.")
with open("file_for_task14", 'r') as file:
    print(random.choice(file.readlines()))

print("16. Write a Python program to assess if a file is closed or not.")
with open("file_for_task14", 'r') as file:
    print(file.closed)
print(file.closed)

print("17. Write a Python program to remove newline characters from a file.")
with open("file_for_task14", 'r') as file:
    list_of_lines = file.readlines()
with open("file_for_task14", 'w') as file:
    for line in list_of_lines:
        new_line = line.strip("\n")
        file.write(new_line)
