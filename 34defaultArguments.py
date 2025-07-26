# default arguments = A default value for certain parameters
#                     default is used when that argument is omitted
#                     make your functions more flexible, reduces # of arguments
#                     1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

def net_price(list_price, discount, tax):
    return list_price * (1 - discount) * (1 + tax)
#net_price(500) this wont work since we need to have an argument for each parameter
print(net_price(500, .1, .07)) #this will work since each parameter is used

def net_price_default(list_price, discount=0, tax=.07): #using default arguments 
    return list_price * (1 - discount) * (1 + tax)
print(net_price_default(500)) #will use the default for discount and tax


def net_price_tax_example(list_price, discount=0, tax=.07): #if we want to use discount default but override tax then we must use it in the argument
    return list_price * (1 - discount) * (1 + tax)
print(net_price_default(500, tax=.09))



#count up function
import time

#def count(start=5, end) #wont work because v
def count(end, start=5): #defaults need to be after positional arguments
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")

count(10)