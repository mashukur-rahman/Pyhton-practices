#get
myDict={
    "name":"Noirit",
    "age":22
}
print(myDict["name"])
print(myDict.get("address", "Dhaka"))
print(myDict.pop("name"))
print(myDict)
print(myDict.update({"age":23}))
print(myDict)
print("age" in myDict)
print("age" in myDict.keys())
print("age" in myDict.values())
print(myDict.items())
