''' Ask the user to type a number
    1. Print the type() of the raw input.
    2. Cast it to a float.
    3. Print the type() again.
'''
number=input('Enter a number: ')  
print("The raw type :",type(number))
number_in_float=float(number)
print("The datatype after casting :",type(number_in_float))