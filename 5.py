def isNumber(number):
    if len(number) == 0:
        return False
    for char in number:
        if ord(char) < 48 or ord(char) > 57:
            return False
    return True

def checkInvalid(nline):
    if not isNumber(nline):
        return True
    if int(nline) < 0 or int(nline) > 4:
        return True
    return False

nline = ""
while nline == "":
    print("input: ", end="")
    nline = input()
    if checkInvalid(nline):
        print("Invalid input please input again.")
        nline = ""

nline = int(nline)
current = 1
for line in range(1, nline + 1):
    print(" " * (nline - line), end="")
    for n in range(current, current + line):
        print(str(n % 10) + " ", end="")
        current += 1
    print("")
