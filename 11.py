print("Example input: 1, 2, 5, 4, 10")
print("Input 10 numbers: ", end="")

numbers = input()
arr = []

def isNumber(number):
    if len(number) == 0:
        return False
    for char in number:
        if ord(char) < 48 or ord(char) > 57:
            return False
    return True

def isSplit(char):
    if len(char) == 0:
        return False
    if ord(char) == 44:
        return True
    return False

def splitNumber(numbers, arr):
    temp = ""
    for number in numbers:
        if isNumber(number):
            temp += number
        elif isSplit(number) and len(temp) != 0:
            arr.append(int(temp))
            temp = ""
        else:
            continue

    if isNumber(temp):
        arr.append(int(temp))

def sortNumber(arr):
    left = 0
    for first in arr:
        right = left + 1
        for second in arr[arr.index(first) + 1:]:
            if first > second:
                arr[right] = first
                arr[left] = second
                first = second
            right += 1
        left += 1

splitNumber(numbers, arr)
sortNumber(arr)
print(arr)
