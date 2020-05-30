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

# Using print statement to display the original & reversed number.
print("The original number is", number)
print ("The reversed number is: ", reverse(number))


# Output:
""" 
Enter your desired string:
Shahzain Ahmed
Enter your desired number:
1 8 C S 8 6
The original string is:  Shahzain Ahmed
The reversed string is:  demhA niazhahS
The original number is 1 8 C S 8 6 
The reversed number is:  6 8 S C 8 1
"""
