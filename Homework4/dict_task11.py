"""
You are given a string . Your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa. For Example:
  Www.HackerRank.com → wWW.hACKERrANK.COM
	  Pythonist 2 → pYTHONIST 2

"""
def convert_letters(string:str):
    string2 = ''
    for letter in string:
        if letter.islower():
            string2 +=letter.capitalize()
        else:
            string2 += letter.lower()
    return string2
print(convert_letters('Www.HackerRank.com'))
print(convert_letters('Pythonist 2'))