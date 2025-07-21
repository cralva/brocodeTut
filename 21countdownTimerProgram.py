import time

'''
myTime = int(input("Enter the time in seconds: "))

for x in range(0, myTime):
    print(x)
    time.sleep(1) #after each iteration we will sleep for 1 second/ myTime = 7 so then after 1, one sec, 2, one sec, and so on
#                  output will be a loop with iterations myTime and 1 sec gap because of time.sleep

# time.sleep(3) # function from the time module that allows pauses, 3 sec pause for this one

print("TIMES UP!")
'''


#if we want to count backwards FIRST WAY
'''
myTime = int(input("Enter the time in seconds: "))

for x in reversed(range(0, myTime)):
    print(x)
    time.sleep(1)

print("TIMES UP!")
'''


'''
#SECOND WAY
myTime = int(input("Enter the time in seconds: "))

for x in range(myTime, 0, -1):
    print(x)
    time.sleep(1)

print("TIMES UP@")
'''


#display digital clock
myTime = int(input("Enter the time in seconds: "))

for x in range(myTime, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIMES UP!")