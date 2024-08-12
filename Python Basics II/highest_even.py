def highest_even(list1):
    evens=[]
    for i in list1:
        if i%2==0:
            evens.append(i)
    evens.sort()
    return evens[-1]
print(highest_even([10,2,3,4,8,11]))