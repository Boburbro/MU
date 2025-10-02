#################################################
############## F O R M A T T I N G ##############
#################################################

yosh = int(input("Yoshingizni kiriting: "))
print(yosh * 365 * 24 * 60)

#################################################

yosh = 30
gap = "Mening yoshim " + str(yosh)
print(gap)

#################################################

gap = "{0} yoshi {1}. {0} ni ishi {2}".format("Temur", 18, "web dasturlash")
print(gap)

#################################################

gap = "{name} yoshi {age}. {name} ni ishi {job}".format(name="Temur", age=18, job="web dasturlash")
print(gap)

#################################################

name = "Temur"
age = 18
job = "web dastulash"

gap = f"{name} yoshi {age * 365 * 24 * 60}. {name} ni ishi {job}"
print(gap)

################################################

gap = "SalOm taLabAlar"

print(gap.lower())
print(gap.upper())
print(gap.capitalize())
print(gap.title())

################################################

gap = "    Aziz Turgunov     "
print(gap.strip())
print(gap.lstrip())
print(gap.rstrip())

################################################

bool_str = ""
bool_val = bool(bool_str)
print(bool_val)

################################################

bool_str = "0"
bool_val = bool(bool_str)
print(bool_val)

################################################

bool_str = 0
bool_val = bool(bool_str)
print(bool_val)

################################################

p = 3.14
num_int = int(p)
print(num_int)

################################################