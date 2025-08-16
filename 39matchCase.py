# Match-case statement (switch): An alternative to using many 'elif' statements
#                           Execute some code if a value matches a 'case'
#                           Benefits: cleaner and syntax is more readable

#using regular elif
def day_of_week(day):
    if day == 1:
        return "It is Sunday"
    elif day == 2:
        return "It is Monday"
    elif day == 3:
        return "It is Tuesday"
    elif day == 4:
        return "It is Wednesday"
    elif day == 5:
        return "It is Thursday"
    elif day == 6:
        return "It is Friday"
    elif day == 7:
        return "It is Saturday"
    else:
        return "Not a valid day"
    
print(day_of_week(2))


#using match case
def day_of_week_match(day):
    match day: #we need to tab everything again. match is the match and day is the case
        case 1:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _: #case _ is what you use instead of and else statement and is called a 'wild card'
            return "Not a valid day"
    
print(day_of_week_match(1))

#new example
def is_weekend(day):
    match day:
        case "Sunday":
            return True
        case "Monday":
            return False
        case "Tuesday":
            return False
        case "Wednesday":
            return False
        case "Thursday":
            return False
        case "Friday":
            return False
        case "Saturday":
            return True
        case _:
            return False
        
print(is_weekend("Monday")) #will be False
print(is_weekend("Saturday")) #will be True
print(is_weekend("Pizza")) #will be false since this will activate the wild card

#using the or logical operator using |
def is_weekend_or(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesay" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False
        
print(is_weekend_or("Monday"))