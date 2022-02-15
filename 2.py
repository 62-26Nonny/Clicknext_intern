s1 = "Maryy"
s2 = "Armyy"

char_s1 = {}
char_s2 = {}

def Uppercase(char):
    if ord(char) >= 95 and ord(char) <= 122:
        return chr(ord(char) - 32)
    else:
        return char

def countChar(text, arr):
    for char in text:
        if Uppercase(char) not in arr:
            arr[Uppercase(char)] = 1
        elif Uppercase(char) in arr:
            arr[Uppercase(char)] += 1

def total_key(dict):
    total = 0
    for key in dict:
        total += 1
    return total

def checkSimilar():
    for key in char_s1:
        if char_s1[key] != char_s2[key]:
            return False
        if total_key(char_s1) != total_key(char_s2):
            return False
        
    return True

countChar(s1, char_s1)
countChar(s2, char_s2)
print(checkSimilar())