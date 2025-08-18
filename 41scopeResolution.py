# variabel scope = where a variable is visible and accessible
# scope resolution = (LEGB) 1. Local -> 2. Enclosed -> 3. Global -> 4. Built-in

def func1():
    a = 1 #variables inside of a function are local variables
    print(a)

def func2():
    b = 2 #local scope/variable 
    print(b)

func1()
func2()
#we cant use local variables in other functions. for ex, if we tried to print b in func1() then it would be a syntax error since we cant use variables in other functions. 'functions cant see in other functions'


def func1():
    x = 1 
    print(x)

def func2():
    x = 2 #even though its the same variable name, the have their own values since its on their own function
    print(x)

func1()
func2()



#enclosed example
def func1():
    x = 1 
    def func2():
        x = 2 #this would print since this is enclosed?????
        print(x)
    func2()

func1()



#globalll

def func1():
    print(x)

def func2():
    print(x)

x = 17 #this will be used since we dont have any local versions. if func1() had x = 1 then it would print 1 for the output of func1

func1()
func2()



#from built-in
from math import e

def func1():
    print(e)

e = 3

func1()