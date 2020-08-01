numbers = [3, 2, 8, 2, 3, 5, 6, 6]

# for number in numbers:
#     while numbers.count(number) > 1:
#         numbers.remove(number)
# print(numbers)

# Alternative way
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
