print("input text: ", end="")
text = input()
reverted = ""
temp = ""

def revertText(text):
    revert_text = ""
    for char in text:
        revert_text = char + revert_text
    return revert_text

for char in text:
    if ord(char) == 32 and len(temp) > 0:
        reverted += revertText(temp) + " "
        temp = ""
    elif ord(char) != 32:
        temp += char

reverted += revertText(temp)
print(reverted)
