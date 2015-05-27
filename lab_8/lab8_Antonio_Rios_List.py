# Antonio Rios
# April 3, 2015
# CS 136 Lab
# Lab 8: Python List Implementation
#######################################################

# Creating a class called Person with First_name, Last_name, and Age as attributes
class Person():

    def __init__(self, first_name, last_name, age):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age

    # Made set functions for attributes
    def set_first_name(self, first_name):
        self._first_name = first_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    def set_age(self, age):
        self._age = age
    # Made get functions for attributes
    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_age(self):
        return self._age
    # Returns a string representation of the Object
    def __str__(self):
        return """
        First Name: {0}
        Last Name: {1}
        Age: {2}""".format(self._first_name, self._last_name,self._age)


#=============== creating three Pearson Objects ======================== #
# Creates 3 persons objects
persons = [Person('Antonio','Rios', 28), Person('Josh', 'Jones', 26), Person('James','Smith',25)]
persons_copy = persons[:]

# Prints object references
print(persons)
print(persons_copy)

#=================== Problem 1===========================================#
print("Problem 1")
print("Items persons list:")
# Shows both lists reference the same object
for person in persons:
    print(person)

print("\nItems persons_copy list:")
for person in persons_copy:
    print(person)

# Changes the age for both persons and persons_copy
print("\nItems persons list:")
for person in persons:
    person.set_age(5)
    print(person)

print("\nItems persons_copy list:")
for person in persons_copy:
    print(person)

#===================== Problem 2 =======================================#
print("Problem 2")
# Creates a Deep copy.  Any changes made to one list does not affect the other
def persons_deep_copy(a_list):
    deep_copy_list = []
    for person in persons:
        deep_copy_list.append(Person(person.get_first_name(), person.get_last_name(), person.get_age()))
    print("Original List:")
    print(a_list)
    print("Deep Copy:")
    print(deep_copy_list)
    return deep_copy_list

deep_copy_list=persons_deep_copy(persons)


#===================== Problem 3 =======================================#
print("Problem 3")
# Changes the age for the persons list (Original list)
print("\nItems persons list:")
for person in persons:
    person.set_age(7)
    print(person)
# The age in deep copy does not get changed
print("\nItems deep_copy_list:")
for person in deep_copy_list:
    print(person)

#===================== Problem 4 =======================================#
print("Problem 4")
# Prints the references to show that they are pointing to a different object
print("References in persons list:")
print(persons)

print("References in deep_copy_list")
print(deep_copy_list)

# Removes the first item in the list
print("After removing first item in persons list:")
del persons[0]
print(persons)
