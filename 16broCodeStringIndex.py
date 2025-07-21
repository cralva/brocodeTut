# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

creditNumber = "1234-5678-9012-3456"

print(creditNumber[2])
print(creditNumber[0:4]) #up to but not including / it will assume 0 so its not needed to input can use [:4] same result
print(creditNumber[5:9])
print(creditNumber[5:]) #will assume you need everything after the

print(creditNumber[-1])  # will give you last value in the list
print(creditNumber[-2]) #second to last value and so on
print(creditNumber[::]) #will assume the entire list

print(creditNumber[::2]) #is step function, will count every two
print(creditNumber[::3]) # step function counting every 3
print(creditNumber[1:13:2]) # the number after the two colons is the step value

#get the last four of the credit card number

print(creditNumber[15:])
#or
lastFour = (creditNumber[-4:])

print(f"XXXX-XXXX-XXXX-{lastFour}")

#reverse characters in string

creditNumber = creditNumber[::-1] #-1 step will reverse the string

print(creditNumber[1:13:2]) #
print(creditNumber)