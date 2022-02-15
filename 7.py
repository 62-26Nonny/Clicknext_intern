def isNumber(number):
    if len(number) == 0:
        return False
    for char in number:
        if ord(char) < 48 or ord(char) > 57:
            return False
    return True

def checkInvalid(seconds):
    if not isNumber(seconds):
        return True
    if int(seconds) < 0:
        return True
    return False

seconds = ""
while seconds == "":
    print("Input seconds: ", end="")
    seconds = input()
    if checkInvalid(seconds):
        print("Invalid seconds please input again.")
        seconds = ""
seconds = int(seconds)

def toMin(seconds):
    mins = seconds // 60
    seconds = seconds % 60
    return mins, seconds

def toHour(mins):
    hours = mins // 60
    mins = mins % 60
    return hours, mins

def isoFormat(seconds):
    iso = ""
    mins, seconds = toMin(seconds)
    hours, mins = toHour(mins)

    if hours == 0:
        iso += "00:"
    elif hours < 10:
        iso += "0" + str(hours) + ":"
    else:
        iso += str(hours) + ":"

    if mins == 0:
        iso += "00:"
    elif mins < 10:
        iso += "0" + str(mins) + ":"
    else:
        iso += str(mins) + ":"
    
    if seconds == 0:
        iso += "00"
    elif seconds < 10:
        iso += "0" + str(seconds)
    else:
        iso += str(seconds)

    return iso

print(isoFormat(seconds))


