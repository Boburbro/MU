################################################
# (1)

name = input("Name? ")
color = input("Color? ")

print("Salom, {name}. Siz yoqtirgan rang - {color}".format(name=name, color=color))

################################################
# (2)

a = 2 
b = 3

print("{a} * {b} = {result1}\n{a} / {b} = {result2}\n{a} + {b} = {result3}\n{a} - {b} = {result4}".format(
    a=a, 
    b=b, 
    result1=a*b, 
    result2=a/b,
    result3=a+b,
    result4=a-b,
))

################################################
# (3)

ism = "Bobur"
yosh = 20
baho = 5.0

print("{ism}, {yosh} yoshda va hozir {baho} olyabdi".format(ism=ism, yosh=yosh, baho=baho))

################################################
# (4)

name = input("Name? ")
print(f"dasdfasdf df asdf {name} sddfdf {name} bsdnsd {name}")

################################################
# (5)

productName = input("Enter the product name: ")
productPrice = int(input("Enter the product price: "))
productCount = int(input("Enter the product count: "))

print("Product name: {name}\nProduct price: {price}\nProduct count: {count}".format(name=productName, price=productPrice, count=productCount))

################################################