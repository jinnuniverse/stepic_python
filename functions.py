#def function_name(argument1, argument2):
#    return argument1 + argument2

#x = function_name(2, 8)
#y = function_name(x, 21)
#print(y)

#print(type(function_name))

#print(id(function_name))

def list_lst(lst):
    result = 0
    for element in lst:
        result += element
    return result

def sum(a, b):
    return a + b

y = sum(14, 29)
z = list_lst([1,2,3])

print(y)
print(z)