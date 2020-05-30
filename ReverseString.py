# Creating a function to reverse a string 
def reverse(string):
    string = "".join(reversed(string))
    return string


# Taking an string as an input from the user.
name = input("Enter your desired string:\n")

# Taking a number as an input from the user.
number = input("Enter your desired number:\n")

# Using print statement to display the original string.
print("The original string  is: ", end="")
print(s)

print("The reversed string is: ", end="")
print(reverse(s))

print ("The reversed number is: ", end="")
print(reverse(a))



