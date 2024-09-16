# Import the 're' module for regular expressions
import re
import msvcrt
# p = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"

print ("Should have at least one number.")
print ("Should have at least one uppercase and one lowercase character.")
print ("Should have at least one special symbol.")
print ("Should be between 8 to 12 characters long and no whitespaces.")

# Prompt the user to input a password and store it in the variable 'p'
p = input("Input your password")

# Set 'x' to True to enter the while loop
x = True

# Start a while loop that continues until 'x' is True
while x:  
    # Check conditions for a valid password:
    # Password length should be between 6 and 12 characters
    if (len(p) < 8 or len(p) > 12):
        break
    # Password should contain at least one lowercase letter
    elif not re.search("[a-z]", p):
        break
    # Password should contain at least one digit
    elif not re.search("[0-9]", p):
        break
    # Password should contain at least one uppercase letter
    elif not re.search("[A-Z]", p):
        break
    # Password should contain at least one special character among '$', '#', '@'
    elif not re.search("[?=.*[@#$%^&+=]", p):
        break
    # Password should not contain any whitespace character
    elif re.search("\s", p):
        break
    else:
        # If all conditions are met, print "Valid Password" and set 'x' to False to exit the loop
        print("Valid Password")
        x = False
        break

# If 'x' remains True, print "Not a Valid Password"
if x:
    print("Not a Valid Password")
