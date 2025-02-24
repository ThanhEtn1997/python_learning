# legal naming
var01 = 10
var_01 = '10'
_var_01 = 'this is new variable'
_Var_01 = 123
VAR_01 = '111111111111111' # constant naming


print(var01, var_01, _var_01, _Var_01, VAR_01)

# illegal naming
# 01var = 10
# var-01 = '10'
# var 01 = 10


# CamelCase
myVar = 'this is camel case'
# snake_case
my_var = 'this is snake case'
# PascalCase
MyVar = 'this is pascal case'

print(myVar, my_var, MyVar)



# Python Variables - Assign Multiple Values

a, b, c = 'monday', 'tuesday', 'wednesday'
print("Many Values to Multiple Variables: ", a, b, c)


x = y = z = 'one value to multiple variables'
print(x, y, z)

ranks = ['First', 'Second', 'Third']
first, second, third = ranks
print("Unpack a Collection: ", first, second, third)


# Output Variables
# The Python print() function is often used to output variables.
weather = 'sunny'
print(weather)

white_space = ' '
moment = 'in the early morning'
print(weather + white_space + moment)

# Global Variables

global_var = 'this is global variable!'

def func_description(description):
    """"""
    print(global_var)
    print("description:", description)

func_description("example print global variable!!!")

## The global Keyword

def func_have_global_var():
    """func_have_global_var"""
    global global_var_01
    global_var_01 = 'this is global variable inside function!!!'

func_have_global_var()
print(global_var_01)
