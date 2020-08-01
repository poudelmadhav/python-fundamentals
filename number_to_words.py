data = {
        "0": "Zero",
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine"
}
phone = input("Phone: ")

numbers_in_words = ''
for digit in phone:
    numbers_in_words += data.get(digit, "!") + " "
print(numbers_in_words)
