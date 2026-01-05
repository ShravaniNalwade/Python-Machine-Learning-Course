from sys import getsizeof

Name=input("Enter your Name:")
print("Name:",Name)
print("Memory Address:",id(Name))
print("Size in bytes:",getsizeof(Name))