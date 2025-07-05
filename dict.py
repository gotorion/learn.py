
# tuple, immutable by default
example_tuple = ("John", 1)
contacts = {
    ("John", 2) : "12345",
    ("Tim", 1) : "32345",
    ("John", 1): "35425"
}
print(contacts)
print(len(contacts))
print("Phone number: " + contacts[example_tuple])

if example_tuple in contacts:
    print("Exist")