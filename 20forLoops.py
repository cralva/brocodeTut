# for loops = execute a block of code a fixed number of times.
#             you can iterate over a range, string, sequence, etc.


'''
#for loop for a range iteration

for x in range(1, 11):
    print(x)

print("Bowls of chips")

for x in reversed(range(1, 11)): #the reversed function will count backwards
    print(x)

print("HAPPY NEW YEAR!")

for x in range(1, 11, 2 ): # third digit is the step. counts every 2 digits
    print(x)
'''


'''
creditCard = "1234-1234-4321-9876"

for x in creditCard:
    print(x)
'''


'''
for x in range(0, 21):
    if x == 13:
        continue # skips over a continuation
    else:
        print(x)

for x in range(0, 21):
    if x ==13:
        break # will stop the program at 13, not included, 12 will be the last number shown
    else:
        print(x)
'''

quilt = (6 * 6)

print(quilt * 3)