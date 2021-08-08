def outerFunc(a, b):
    a = int(a)
    b = int(b)
    square = a ** 2

    def innerFunc(a, b):
        return a + b

    add = innerFunc(a, b)
    return add + 5


x = input("Enter Numb1: ")
y = input("Enter Numb2: ")
res = outerFunc(x, y)
print(res)
