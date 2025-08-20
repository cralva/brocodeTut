# print(__name__) #first ex

#------------------------------------
from script1_40 import *

def favorite_drink(drink):
    print(f"My favorite drink is {drink}")

def main(): 
    print("This is script 2")
    favorite_food("Pizza")
    favorite_drink("Water")
    print("Goodbye")

if __name__ == "__main__":
    main() #added this last to show that that will all get called as long as this is true