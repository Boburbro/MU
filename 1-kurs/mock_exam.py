n = 6
while n > 0:
    n -= 1
    if n == 4:
        continue
    print("n =", n)
    if n == 2:
        break
    print("after loop:", n)