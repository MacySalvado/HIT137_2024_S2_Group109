# To get the key

total = 0
for i in range(5):
    for j in range(3):
        if i + j == 5:
            total += i + j
        else:
            total -= i - j

counter = 0
while counter < 5:
    if total < 13:
        total += 1
    elif total > 13:
        total -= 1
    else:
        counter += 2

# add print()  to get the result printed
print(total)


# the code is working! :)
# the result for total is: 13