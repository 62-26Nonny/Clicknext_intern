arr = [1, 2, 3, 4, 5, 6, 7, 1, 4]
sum = 5
used = []
for first_value in arr:
    if first_value < sum:
        for second_value in arr[arr.index(first_value) + 1:]:
            if first_value + second_value == sum and second_value not in used:
                print(str(first_value) + "," + str(second_value))
                used.append(first_value)
                used.append(second_value)
                break

                 