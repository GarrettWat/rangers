# Q 1 Write a function to Print "Hello_USERNAME!"

from operator import truediv


def hello_name(user_name):
    print("hello_" + user_name.upper() + "!")

hello_name("garrett")

#Q 2 Print the first odd numbers between 1 and 100

def first_odds():
    for i in range(1,101):
        if i % 2 == 1:
            print(i)
first_odds()
        
#first odds

def first_odds2():
    print(list(range(1,101,2))) 
first_odds2()

#Q3 Write a Function That Returns the max num in a given list

def max_num_in_list(a_list):
    max = a_list[0]

    for number in a_list:
        if max < number:
            max = number
    return max

print(max_num_in_list([2,3,5,8,12]))

#Q4 Write a function to return (true) if the given year is a leap year or (false).

def is_leap_year(a_year):
    if a_year % 100 != 0 and a_year % 4 == 0 or a_year % 400 == 0:
        return True
    else:
        return False
print(is_leap_year(2022))
print(is_leap_year(2020))


#Q5 Write a function that checks if all the numbers in a list are consecutive.

def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list),max(a_list)+1))

print(is_consecutive([3,4,5,6,7,8]))
print(is_consecutive([3,4,5,4,6,7,8]))