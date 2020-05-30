# Creating a function to reverse a string 
def reverse(string):
    string = "".join(reversed(string))
    return string


# Declaring and Initializing .
s = "Shahzain Ahmed"
a = "86"

print("The original string  is: ", end="")
print(s)

print("The reversed string is: ", end="")
print(reverse(s))

print ("The reversed number is: ", end="")
print(reverse(a))



