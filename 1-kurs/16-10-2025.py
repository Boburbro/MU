age = input("Enter your age: ")

while not age.isdigit():
    age = input("It must be an integer: ")

age = int(age)

if age < 18:
    print("You are a minor")
elif 18 <= age < 65:
    print("You are an adult")
elif age >= 65:
    print("You are a senior citizen")
else:
    print("Idk bro, are you alive??")
