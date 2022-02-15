def isNumber(number):
    if len(number) == 0:
        return False
    for char in number:
        if ord(char) < 48 or ord(char) > 57:
            return False
    return True

def checkInvalid(cost):
    if not isNumber(cost):
        return True
    if int(cost) < 0 or int(cost) >= 1000:
        return True
    return False

cost = ""
while cost == "":
    print("input product cost: ", end="")
    cost = input()
    if checkInvalid(cost):
        print("Invalid cost please input again.")
        cost = ""

cost = int(cost)
change = 1000 - cost
print("change:", change)

def cashier(change):
    if change // 500 > 0:
        print("500: " + str(change // 500))
        change = change % 500
    if change // 100 > 0:
        print("100: " + str(change // 100))
        change = change % 100
    if change // 50 > 0:
        print("50: " + str(change // 50))
        change = change % 50
    if change // 10 > 0:
        print("10: " + str(change // 10))
        change = change % 10
    if change // 5 > 0:
        print("5: " + str(change // 5))
        change = change % 5
    if change // 1 > 0:
        print("1: " + str(change // 1))
        change = change % 1

cashier(change)