# use *args when the number of arguments is indefinite
#args converts the input to a tuple
def summation(*args):
    
    return sum(args)

print(summation(1,2,3))


# kwargs converts the defined argument into a dictionary 
def summation2(**kwargs):
    
    print(kwargs)

print(summation2(num1=1,num2=2, num3=3))
