#strings are immutable 
# str() can be used convert a integr to a string object
string_1 = "Antony"
string_2 = "Micheal"

# Concatanating 2 strings

string_3 = string_1 +" "+ string_2
print(string_3)

# length 

print("length of the string is" + " "+str(len(string_3)))

# indexing.
print(string_1[1:4])

# negative indexing.
print(string_1[:-1])

#Slicing
print("After slicing "+string_1[1:] + string_2[1:])
print("Reversing using Slicing: "+ string_3[::-1])

# to upper and to lower
print("Upper case: "+string_3.upper())
print("Lower: " + string_3.lower())

# Capitalize
print("antony capitalized: " +"antony".capitalize())

# count
print("Count of 'n' in antony = " + str("antony".count("n")))

# endswith checks if a string ends with a particularr value
print(string_1.endswith("y"))
print(string_1.endswith("d"))

# find() - reeturns the first occurance index of the value
print(string_1.find("t"))

# isalnum - checks if the string is alnum

# isdigit -> checks if the string/charecter is a digit
# islower()
#isupper()
#isnumeric()

#split()
print(string_3.split())

#swapcase
print("SwaPcAsE".swapcase())

# Replace
#JOIn

# String formatting
val = 2.00040
print(f"hi {string_1} {string_2}. How are you {val}")