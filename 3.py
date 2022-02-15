arr = [1 ,2 ,4 ,6 ,9 , 5, 8, 11]
start = ""

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

sortNumber(arr)

def findLengh(arr):
    total = 0
    for elm in arr:
        total += 1
    return total

for index in range(0, findLengh(arr)):
    next_index = (index + 1) % len(arr)
    endl = ", "
    if findLengh(arr) - index - 1 == 0:
        endl = ""
    if arr[index] + 1 == arr[next_index] and start == "":
        start = index
        continue
    elif arr[index] + 1 == arr[next_index] and start != "":
        continue
    elif arr[index] + 1 != arr[next_index] and start != "":
        print(str(arr[start]) + '-' + str(arr[index]), end=endl)
        start = ""
    else:
        print(str(arr[index]), end=endl)
    
