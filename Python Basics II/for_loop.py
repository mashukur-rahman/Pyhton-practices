#sum of all inputs
numbers=input("Enter the numbers:")
numbers_list=numbers.split(",")

sum1=0
for i in range (len(numbers_list)):
    sum1+=int(numbers_list[i])
print(sum1)
