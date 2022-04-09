dictmap = {
    "1":"Amit",
    "2":"Suresh",
    "3":"Ram"
}
#Printing the Dictionary
print(dictmap)
#Feching a value for a given key
x = dictmap.get("2")
print(x)

#Update a value
dictmap.update({"1":"Mahesh"})

#Adding K-V pair
dictmap.update({"4":"Raghav"})

#Removing a value for a given key
dictmap.pop("2")

#Removes last inserted element
dictmap.popitem()

