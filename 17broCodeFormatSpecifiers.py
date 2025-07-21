# format specifiers = {value.flags} format a value based on what
#                             flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma seperator

price1 = 3989.14159
price2 = -9879.65
price3 = 1276.34

print(f"Price 1 is ${price1:.3f}") # round decimal points (whatever number the flag is)
print(f"Price 1 is ${price2:.1f}")
print(f"Price 1 is ${price3:.3f}") #will add in zero if variable doesnt have enough decimal points

print(f"Price 1 is ${price1:10}") # has 10 spaces to display the output. will be blank to make the last number be 10
print(f"Price 1 is ${price2:8}")
print(f"Price 1 is ${price3:20}")

print(f"Price 1 is ${price1:010}") #will be zero padded, sinmilar to above except the empty spaces will be filled with 0's
print(f"Price 1 is ${price2:010}")
print(f"Price 1 is ${price3:010}")

print(f"Price 1 is {price1:<10}") # will push the numbers to the left and have padding to the right
print(f"Price 1 is {price2:<10}")
print(f"Price 1 is {price3:<10}")

print(f"Price 1 is {price1:>10}") # will push the numbers to the right and have padding to the left
print(f"Price 1 is {price2:>10}")
print(f"Price 1 is {price3:>10}")

print(f"Price 1 is {price1:^10}") # will center the value, empty padding to the left and right
print(f"Price 1 is {price2:^10}")
print(f"Price 1 is {price3:^10}")

print(f"Price 1 is {price1:+}") #will input a positive symbol
print(f"Price 1 is {price2:+}") #if neg value, will input neg symbol
print(f"Price 1 is {price3:+}")

print(f"Price 1 is {price1: }")
print(f"Price 1 is {price2: }") #make the values lined up evenly
print(f"Price 1 is {price3: }")

print(f"Price 1 is {price1:,}") #will add a comma at the thousands place
print(f"Price 1 is {price2:,}")
print(f"Price 1 is {price3:,}")

print(f"Price 1 is {price1:+,.2f}") #combining flags
print(f"Price 1 is {price2:+,.2f}")
print(f"Price 1 is {price3:+,.2f}")