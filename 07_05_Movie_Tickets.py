number = input("If under the age of 3, the ride will be free")
number = int(number)
if number % 3 <= 0:
    print(f"\nThen {number} the ride is free.")
else:
    print(f"\nThe {number} ride cost money")
number = input("If their age is between 3 to 12, the ride costs $10")
number = int(number)
if number % 3 == 12:
    print(f"\nThen {number} the ride costs $10 ")
else:
    print(f"\nThe {number} ride costs $12")