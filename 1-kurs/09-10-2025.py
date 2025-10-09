#################################################
################### L I S T S ###################
#################################################

colors = [
    "Red",
    "Blue",
    "Green",
    "Yellow",
    "Black",
    "White",
]

print(colors[0])
print(colors[-1])

#################################################

colors[2] = "purple"
print(colors)

#################################################

grocery_list = ["Non", "Sut", "Yog'", "Shakar", "Choy", "Tuxum"]

print("Xaridlar soni:", len(grocery_list))

#################################################

grocery_list.append("cheese")
print(grocery_list)

#################################################

grocery_list.insert(0, "fruits")
print(grocery_list)

#################################################

grocery_list.remove("Tuxum")
print(grocery_list)

#################################################

item = grocery_list.pop(2)
print(grocery_list)
print(item)

#################################################

numbers = [3, 5, 2, 5, 6, 62, 56, 7]
numbers.sort()
print(numbers)

#################################################

numbers.reverse()
print(numbers)

#################################################

numbers = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
print(numbers)

#################################################

copied_grocery_list = grocery_list.copy()
copied_grocery_list.append("juice")
print(grocery_list)
print(copied_grocery_list)