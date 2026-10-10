# # D2.1

# a = 3
# b = a
# a = 7
# print(b)  # Output: 3

# # D2.2

# name = input("Name: ")
# print("Hi,", name, "!") # Output: Hi, Ali !

# ====================================================================================

# # Ex 2.1

# name = input("Enter your name: ")
# city = input("Enter your city: ")
# print("Salom, {} from {}".format(name, city))  # Output: Salom, Ali from Tashkent 

# # Ex 2.2

# n1 = float(input("Enter a number: "))
# n2 = float(input("Enter another number: "))
# area = n1 * n2
# perimeter = 2 * (n1 + n2)

# print("Area =", area, "Perimeter =", perimeter)  # Output: Area = 24.0 Perimeter = 20.0

# # Ex 2.3

# x, y = int(input("Enter x: ")), int(input("Enter y: "))
# x, y = y, x

# print("x = {}, y = {}".format(x, y))  # Output: x = 9, y = 4

# ====================================================================================

# # Ex 2.4

# x, y, z = float(input("Enter a number: ")), float(input("Enter another number: ")), float(input("Enter one more number: "))
# sum = x + y + z

# print("Total =", sum)  # Output: Total = 23500.0

# # Ex 2.5

# name = input("Enter a name: ")
# animal = input("Enter an animal: ")
# number = input("Enter a number: ")

# print("{name} bir kun {animal} bilan {number} ta "
#       "somsa yebdi. Keyin {animal} pulini to'lamay "
#       "qochib ketibdi.".format(
#           name=name, animal=animal, number=number
#       )) 

# ====================================================================================

# # Ex 2.1

# name = input("Enter your name: ")
# print("Salom,", name, "!")  # Output: Salom, Ali !

# # Ex 2.2

# n1 = int(input("Enter a number: "))
# n2 = int(input("Enter another number: "))

# print("Sum: ", n1 + n2)  # Output: Sum: 13
# print("Difference: ", n1 - n2)  # Output: Difference: -5
# print("Product: ", n1 * n2)  # Output: Product: 36

# # Ex 2.3

# age = int(input("Enter your age: "))
# print("{}".format(age * 365)) # Output: 3935

# # Ex 2.4

# km = float(input("Enter distance in kilometers: "))
# m = km * 1000
# cm = m * 100

# print("{} m, {} cm".format(m, cm))  # Output: 2000.0 m = 200000.0 cm

# # Ex 2.5

# n = int(input("Enter a number: "))
# area = n * n
# perimeter = 4 * n

# print("Area =", area, "Perimeter =", perimeter)  # Output: Area = 25 Perimeter = 20

# # Ex 2.6

# distance = float(input("Enter distance in kilometers: "))
# speed = float(input("Enter speed in km/h: "))
# time = distance / speed

# print("Time =", time, "hours")  # Output: Time = 2.0 hours

# # Ex 2.7 

# n1, n2, n3 = int(input("Enter first number: ")), int(input("Enter second number: ")), int(input("Enter third number: "))
# total = n1 + n2 + n3
# average = total / 3

# print("Total =", total, "Average =", average)  # Output: Total = 60 Average = 20.0

# # Ex 2.8

# name = input("Enter a name: ")
# animal = input("Enter an animal: ")
# place = input("Enter a place: ")
# food = input("Enter a food: ")

# print(f"{name} went to {place} with a {animal}.")
# print(f"They ate some {food} and went home.")

# # Ex 2.9 

# a, b, c = int(input("Enter first number: ")), int(input("Enter second number: ")), int(input("Enter third number: "))

# a, b, c = c, a, b

# print(a, b, c)  # Output: 3, 1, 2

# # Ex 2.10

# total_minut = int(input("Enter total minutes: "))
# hours = total_minut // 60
# minutes = total_minut % 60

# print("{hours} h {minutes} m".format(hours=hours, minutes=minutes))  # Output: 2 h 15 m

# # Ex 2.11

# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")

# print("{}. {}".format(first_name[0], last_name[0]))  # Output: A. V

# # Ex 2.12

# som = float(input("Enter amount in som: "))
# rate = float(input("Enter exchange rate: "))
# usd = som / rate

# print("Amount in USD: {:.2f}".format(usd))  # Output: Amount in USD: 100.00

# # Ex 2.13

# weight = float(input("Enter your weight in kg: "))
# height = float(input("Enter your height in meters: "))
# bmi = weight / (height ** 2)

# print("Your BMI is: {:.3f}".format(bmi))  # Output: Your BMI is: 22.857

# # Ex 2.14
# """
# START
#     CURRENT_PIN = 1234
#     BALANCE = 1000.0
#     INPUT entered_pin
#     IF entered_pin != CURRENT_PIN THEN
#         PRINT "Incorrect PIN"
#         EXIT
    
#     INPUT withdraw_amount
#     IF withdraw_amount <= 0 THEN
#         PRINT "Invalid amount"
#         EXIT
    
#     IF withdraw_amount > BALANCE THEN
#         PRINT "Insufficient funds"
#         EXIT
    
#     BALANCE = BALANCE - withdraw_amount
#     PRINT "Take your cash:", withdraw_amount
#     PRINT "Remaining balance:", BALANCE
# FINISH  
# """

# # Ex 2.15 Shart: Sonlari kiritmadan hisoblangan hikoya (kelasi yil yoshi, tug‘ilgan yili va h.k.).

# current_year = 2026

# name = input("Ismingizni kiriting: ")
# age = int(input("Yoshingizni kiriting: "))

# birth_year = current_year - age
# next_year_age = age + 1

# print(f"Salom, {name}! Siz {birth_year} yilda tug‘ilgansiz va kelasi yil siz {next_year_age} yoshga to‘lasiz.")
