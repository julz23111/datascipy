#1.1 Create and read a dictionary
#Creat a dictionary
contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",#None
    "Charlie": "555-8765"
}

# print(type(contacts))

#1.2 Access Dictionary Values
k = "Alice"
# print(contacts["k"])  
# print(contacts["Bob"])

# #1.3 Key Error
# print(contacts['alice'])

#1.4 Check using in operator
# if "alice" in contacts:
#     print(contacts['alice'])
# else:
#     print("not found")

#1.5 Safe access using get() method
# print(contacts.get("alice", "not found"))

#2.1 Add new keyvalue pair
contacts["David"] = "555-4321"
contacts['Alice'] = "555-0000"
contacts['alice'] = "555-1111"
print(contacts)

#2.2 Update existing keyvalue pair


#2.3 Remove keyvalue pair using del
# del contacts['alice']
# print(contacts)

#2.4 Remove keyvalue pair using pop()
# removed =contacts.pop('alice', 'error on key not found')
# print(removed)

#2.5 Getting all values and keys
# allKeys = contacts.keys()
# allValues = contacts.values()

# print(allKeys)
# print(type(allKeys))

# allItems = contacts.items()
# print(allItems)

#2.6  iterate through dictionary
for k in contacts.keys():
    print(k)
for v in contacts.values():
    print(v)
for i in contacts.items():
    print(i)
for k, v in contacts.items():
    print(f"The key is {k} and the value is {v}")