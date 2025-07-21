# python compound interest calc



princ = 0
rate = 0
time = 0

while princ <= 0:
    princ = int(input("Enter the principle amount: "))
    if princ <= 0:
        print("Principle cant be less than or equal to zero") #why is this not an infinite loop?

while rate <= 0:
    rate = int(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest rate cant be less than or equal to zero")

while time <= 0:
    time = int(input("Enter the in years: "))
    if time <= 0:
        print("Time cant be less than or equal to zero")

total = princ * pow((1 + rate / 100), time)

print(f"Balance after {time} year/s: ${total:.2f}")




# two ways of writing whats above first one is below

'''
princ = 0
rate = 0
time = 0

while princ < 0: #will skip over everything and go to the bottom to print total. its because none of the while loops are true 
    princ = int(input("Enter the principle amount: "))
    if princ < 0:
        print("Principle cant be less than 0")

while rate < 0:
    rate = int(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate cant be less than 0")

while time < 0:
    time = int(input("Enter the in years: "))
    if time < 0:
        print("Time cant be less than zero")

total = princ * pow((1 + rate / 100), time)

print(f"Balance after {time} year/s: ${total:.2f}")
'''




'''
princ = 0
rate = 0
time = 0

while True: #instead of comparing to a variable but will be infinite
    princ = int(input("Enter the principle amount: "))
    if princ < 0:
        print("Principle cant be less than zero")
    else:
        break #need break statement to get out of it so it wont be infinite

while True:
    rate = int(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate cant be less than zero")
    else:
        break

while True:
    time = int(input("Enter the in years: "))
    if time < 0:
        print("Time cant be less than zero")
    else:
        break

total = princ * pow((1 + rate / 100), time)

print(f"Balance after {time} year/s: ${total:.2f}")
'''