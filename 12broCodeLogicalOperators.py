# logical operator = evaluate multiple conditions (or, and, not)
#                    or = at least one condition must be True
#                    and = both conditions must be True
#                    not = inverts the condition (variable value gets inverted) (not False, not True)

'''
temp = 25
isRaining = False

if temp > 35 or temp < 0 or isRaining: #
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")
'''

'''
temp = -5
isRaining = True

if temp > 35 or temp < 0 or isRaining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")
'''
'''


temp = 25
isSunny = True

if temp >= 28 and isSunny:
    print("It is hot outside")
    print("It is sunny")
elif temp <= 0 and isSunny:
    print("It is COLD outside")
    print("It is sunny")
elif temp < 28 and temp > 0 and isSunny: #can also use 28 > temp > 0 and isSunny
    print("It is warm outside")
    print("IT is sunny")
'''

temp = 25
isSunny = False

if temp >= 28 and isSunny:
    print("It is hot outside")
    print("It is sunny")
elif temp <= 0 and isSunny:
    print("It is COLD outside")
    print("It is sunny")
elif temp < 28 and temp > 0 and not isSunny: #can also use 28 > temp > 0 and isSunny
    print("It is warm outside")
    print("IT is sunny")