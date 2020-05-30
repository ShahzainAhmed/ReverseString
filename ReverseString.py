# Creating a function to reverse a string 
def reverse(string):
    string = "".join(reversed(string))
    return string


# Taking an string as an input from the user.
name = input("Enter your desired string:\n")

# Taking a number as an input from the user.
number = input("Enter your desired number:\n")

# Using print statement to display the original & reversed string.
print("The original string is: ", name)
print("The reversed string is: ", reverse(name))
