"""Classes are a way to create custom datatypes"""
#example - creating a Student data type - even int is a class

class Computer:
    """Simple class""" 
    def spec(self):
        """Simple method"""
        print("this is an i5 machine with 8gb RAM")

c1 = Computer() # creating a datatype computer

print(type(1))
print(type(c1))


c1.spec() # c1 is being passed as a parameter.

