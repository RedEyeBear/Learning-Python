## PYTHON BASICS ##

## BASIC MATHEMATICS ##
print(2+1)  # Addition Calculation
print(2-1)  # Subtraction Calculation
print(2*3)  # Multiplication Calculation
print(4/2)  # Division Calculation
print(7 % 4)  # Reminder Calculation
print(4 ** 3)  # Power Calculation
print(2 + 10 * 10 + 3)  # Complex Calculation
print((2+10) * (10+3))  # Parantheis Calculation

# Checking variable type
a = 10
print(type(a))
b = 15.5
print(type(b))
c = "Hello World"
print(type(c))

# Giving variable names (variable assignment)
my_income = 100000
tax_rate = 0.25
my_taxes = my_income * tax_rate
print(my_taxes)

# Strings
print("Hello World one")
print("Hello world Two")

# Starting New Line using \n function
print('Hello \n World \n One')

# Giving 4 spaces that is a tab using \t function
print('Hello World \t Two')

# Checking length of the string using len function (It counts spaces as well)
print(len('I am Sumit'))

# Indexing:- Positive or Negative indexing to grab letter from the string
my_string = "Hello World"
print(my_string[2])
print(my_string[-3])

# Slicing:- grabing letter from a string
my_string = "abcdefghijk"
print(my_string[2:])
print(my_string[:5])
print(my_string[2:6])
print(my_string[::-1])  # Reversing the string

# Formatting Strings using .format method
print("Sumit {0} {2} {3} {1}" .format("is", "boy", "a", "good"))

# Formatting Strings using f string method
name = "Sumit"
age = 33
print(f'{name} is {age} years old.')

# List in Pyhton #
# Lists are created using braces []
mylist = ['one', 'two', 'three']
print(mylist)
print(mylist[2])
another_list = ['four', 'five']
print(another_list)

# adding two lists
new_list = mylist + another_list  # Concat
print(new_list)

# Slicing of a list
print(new_list[2:4])  # Slicing

# using {append} for adding a new list item at the end
new_list.append('six')
print(new_list)

# using {pop} for popping/removing item from the list
new_list.pop(0)
print(new_list)

# using {sort} for soritng lists
new_list = ['a', 'k', 'd', 'i', 'b']
num_list = [5, 8, 3, 1, 9]
new_list.sort()   # Sorting of strings
print(new_list)
num_list.sort()  # Sorting of numbers
print(num_list)

# using {reverse} for reversing a list
num_list.reverse()
print(num_list)

# Dictionaries in Pyhton #
# Dictionaries are created using curly braces {}
price_lookup = {'apple': 250, 'bananas': 60, 'oranges': 150, 'grapes': 120}
print(price_lookup['apple'])
print(price_lookup['bananas'])
print(price_lookup['oranges'])
print(price_lookup['grapes'])

## using dictionaries with dictionaries ##
list_dict = {'Name': "Sumit", 'Age': 33, "Education": {
    '1st': "MBA", "2nd": "BSc", "3rd": "PGDEE"}}
print(list_dict["Name"])  # calling individual items of key values
print(list_dict['Education']['3rd'])
list_dict['Name'] = "Neha"  # replacing key value ##
print(list_dict)
print(list_dict.values())   # prinitng list values
print(list_dict.items())   # printing list items

# Tuples in Python
# Tuples are created using paranthesis ()
# Tuples does not support item assignment like lists do
t = (1, 2, 3)  # tuples using numbers
print(type(t))
t = ('one', 'two', 'three')  # Tuples using string
t = ('one', 2)  # Tuples using both strings & numbers
print(t[0])  # Tuples slicing same as lists

## Sets in Python
# A set contains unique values inside :- same value is not repeated again
myset = set()
myset.add(1)  # Adding value insdie a set
print(myset)
myset.add(2)  # adding another value inside a set
print(myset)
# second time 2 does not get add in the set as SET only accept unique values
myset.add(2)
print(myset)
print(type(myset))

## Booleans in Pyhton
# True always write with capitalized T
# False always write with capitalized F
x = True
print(type(x))
print(1 > 2)
print(5 > 3)
print(2 == 2)
