import personClass as pc

generic_person = pc.Person("Bob", "123 Rd", 1234567890)

specific_person = pc.Customer("Joe", "321 St", 9876543210, 1234, True)

print()
generic_person.print_person()
print()
specific_person.print_person()
print()
