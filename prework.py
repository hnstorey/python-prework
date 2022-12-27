# Question 1
# Write a function to print "hello_USERNAME!" 
# USERNAME is the input of the function. 

def hello_name(user_name=''):
    ###Display a simple greeting using user input.###
    user_name = input("What is your first name? ")
    print("Hello, " + user_name.title() + "!")

hello_name()

# Question 2
# Write a python function, first_odds that prints the odd numbers 
# from 1-100 and returns nothing.

def first_odds():
    ###Print the odd numbers from 1-100.###
    odd_nums = list(range(1,100,2))
    print(odd_nums)

first_odds()

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list.

def max_num_in_list(a_list):
    ###Print the maximum number of a given list.###
    print(max(a_list))

max_num_in_list([101, 65, 39, 6, 8])

# Question 4
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).

def is_leap_year(a_year):
    ###Return True if a given year is a leap year.###
    a_year = int(a_year)
    if a_year % 4 == 0:
        print('True')
    else:
        print('False')
    
is_leap_year("2022")

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.

def is_consecutive(a_list):
    ###Check to see if the given numbers are consecutive.###
    if len(a_list) - 1 == max(a_list) - min(a_list):
        print(True)
    else:
        print(False)

is_consecutive([4,6,5,3])