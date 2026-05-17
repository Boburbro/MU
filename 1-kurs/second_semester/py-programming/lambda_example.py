def square(x):
    return x ** 2

square_lambda = lambda x: x ** 2

print(square(5))  
print(square_lambda(5))

def add(x, y):
    return x + y

add_lambda = lambda x, y: x + y

print(add(3, 4))
print(add_lambda(3, 4))

def maximum(a, b):
    return a if a > b else b

maximum_l = lambda a, b: a if a > b else b

print(maximum(1,2))
print(maximum_l(1,2))

# 4.Son juft yoki toqligini tekshirish
def is_even(n):
    return n % 2 == 0

is_even_l = lambda n: n % 2 == 0

print(is_even(7))
print(is_even_l(7))

# 5. Matnni teskarisiga aylantirish
def reverse_string(s):
    return s[::-1]

reverse_string_l = lambda s: s[::-1]

print(reverse_string("qqasdssa"))
print(reverse_string_l("qqasdssa"))

# 6. Matn uzunligini topish
def string_length(s):
    return len(s)

string_length_l = lambda s: len(s)

print(string_length("a"))
print(string_length_l("a"))

# 7. Palindrome tekshirish
def is_palindrome(s):
    return s == s[::-1]

is_palindrome_l = lambda s: s == s[::-1]

print(is_palindrome("kiyik"))
print(is_palindrome_l("kiyik"))

# 8. Celsius → Fahrenheit o‘tkazish
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

celsius_to_fahrenheit_l = lambda c: (c * 9/5) + 32

print(celsius_to_fahrenheit(3))
print(celsius_to_fahrenheit_l(3))

# 9. So‘zning birinchi harfini olish
def first_letter(word):
    return word[0]

first_letter_l = lambda word : word[0]

print(first_letter("SAlonm"))
print(first_letter_l("SAlonm"))

# 10.  Ro‘yxatdagi elementlarni 2 ga ko‘paytirish
def multiply_list(lst):
    return [x * 2 for x in lst]

multiply_list_l = lambda lst: [x * 2 for x in lst]

print(multiply_list([2,3]))
print(multiply_list_l([2,3]))

# 11. 
def calculate_power(base, exponent):
    return base ** exponent + (base * exponent) - (base / (exponent + 1))

calculate_power_l = lambda base, exponent: base ** exponent + (base * exponent) - (base / (exponent + 1))


print(calculate_power(2,3))
print(calculate_power_l(2,3))

# 12. Savol:
# Ro‘yxatdagi sonlarni o‘zgartiring: juftlar kvadrat, toqlar kub bo‘lsin.
# Input: [1, 2, 3, 4]
# Output: [1, 4, 27, 16]

cal = lambda items: [
    n**2 if n % 2 == 0 
    else n**3 
    for n in items
]
print(cal([1,2,3,4,5]))


# 12.5.
# cal = lambda items: [
#     n**2 if n % 2 == 0 
#     else n**3 if n % 3 == 0 
#     else n**4 for n in items
# ]
print(cal([1,2,3,4,5]))

cal = lambda items: max(items, key=len)
print(cal(("hello", "hi", "evalution"))) 

# 14. Savol:
# Uchta sonning eng kattasini qaytaring.
# Input: (3, 7, 5)
# Output: 7

cal = lambda items: max(items)
cal((3,7,5))

# 15. Lambda formatiga otkazib berin: 
def check_conditions(x):
  if x > 10:
    return x * 10
  elif x < 5:
    return x * 5
  else:
    return x


check_conditions_l = lambda x: x * 10 if x > 10 else x * 5 if x < 5 else x 

print(check_conditions(11))
print(check_conditions_l(11))
