'''Prework for Dan Rodriguez'''
# Q1: Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
def hello_name(user_name):
    '''Print hello message from Q1.'''
    print(f"Hello, {user_name.title()}!")

# Q1 test
hello_name('danilo')

# Q2: Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing.
def first_odds():
    ''''Print odd numbers from 1 to 100'''
    for i in range(1, 100, 2):
        print(i, end=" ")
    print()
    
# Q2 test
first_odds()

# Q3: Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
def max_num_in_list(a_list):
    '''Return the max number of a given list'''
    return max(a_list)

# Q3 test
x = list(range(1, 11))
print(f"Max number in list: {max_num_in_list(x)}")

# Q4: Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400.
# The return should be boolean Type (true/false).
def is_leap_year(a_year):
    '''Return boolean for if year provided is a leap year or not.'''
    if (a_year % 4 == 0):
        if (a_year % 100 != 0):
            return True
        elif (a_year % 100 == 0) & (a_year % 400 == 0):
            return True
        else:
            return False
    else:
        return False

# Q4 test
year = [2000, 1592, 1716, 2003, 1948]
for i in year:
    print(f"Is {i} a leap year? {is_leap_year(i)}")

# Q5: Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
def is_consecutive(a_list):
    '''Return boolean for if list is consecutive or not.'''
    a_list.sort()
    x = a_list[0]
    flag = True
    for i in a_list:
        if i==x:
            x+=1
        else:
            flag = False
    return flag

# Q5 test
y = list(range(3,10))
z = [7,6,8]
print("\nAre the numbers in the list consecutive?" + 
        f"\n\tList: {y}" +
        f"\n\tT/F: {is_consecutive(y)}"
        )
y.remove(6)
print("Are the numbers in the list consecutive?" + 
        f"\n\tList: {y}" +
        f"\n\tT/F: {is_consecutive(y)}"
        )
print("Are the numbers in the list consecutive?" + 
        f"\n\tList: {z}" +
        f"\n\tT/F: {is_consecutive(z)}"
        )