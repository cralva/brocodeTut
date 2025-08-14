def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

def add_print(*args):
    total = 0
    for arg in args:
        total += arg
    print(total)

testOne = add(4, 5, 6)
print(testOne)

add_print(4, 5, 6)