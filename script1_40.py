# print(dir()) #will print off all of the attributes / variables
# print(__name__) #will give us a string of "__main__" and this is only because we are in the file where __name__ is getting called. if we imported this file then __main__ will be replaced with the name of the file

# if __name__ == "__main__": #come back to this
#     main()



# from script2_40 import * #* means everything #first ex

# print(__name__) #this will print out __main second and script2_40 first since the importing immediately called the print and since it was in a different file then the file name was shown instead of __main__. call the __name__ in this file is why the __main__ was printed

#-------------------------------------------------
def favorite_food(food):
    print(f'your favorite food is {food}')
def main():
    print("This is script 1")
    favorite_food("Pizza")
    print('Goodbye')

if __name__ == "__main__":
    main() #if it wasnt for this if statement then everything in this program would be ran immedately when it was imported into to a different file. this makes it so you need to manually call each function for it to run. If we run this program while in it then the main() function will be executed since the if statemnt is true