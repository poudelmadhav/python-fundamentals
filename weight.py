weight = input("Enter your weight: ")
unit = input("(L)bs or (K)g: ")

if unit == "L":
    kg = int(weight) * 0.45
    print(f"Weight: {kg} kg")
else:
    pounds = int(weight) / 0.45
    print(f"Weight: {pounds} pounds")
