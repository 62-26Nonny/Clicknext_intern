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
    if int(nline) < 0:
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
i = 0
for line in range(nline * 2 - 1, 0, -2):
    print((" " * i) + ("*" * line))
    i += 1