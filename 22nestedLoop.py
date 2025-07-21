# nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:


'''
#what do we do if we want to have this loop print 3 times. we could copy and print it three times but a better way
for x in range(1, 10):
    print(x, end = "") #for loop iterations automatically end \n which gives it a new line. the end = "" replaces \n with a space so its all on the same line
'''


'''
#instead of printing the loop three seperate times we can nested loop

for x in range(3):
    for y in range(0, 10):
        print(y, end = "")
'''


'''
for x in range(3): 
    for y in range(0, 10):
        print(y, end = "")
    print() # this will add a new line between iteration lists
'''


# print a rectangle of symbols

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()