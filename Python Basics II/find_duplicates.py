my_list=["a", "b", "c", "c", "a", "d"]

duplicates=[]

for i in my_list:
    if my_list.count(i)>1:
        if i not in duplicates:
            duplicates.append(i)

print(duplicates)