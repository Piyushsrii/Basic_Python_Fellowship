import string

str1 = "Hello, \n"  # Variable to store the string "Hello"
str2 = "How are you"  # Variable to Store the String "How are you"
str3 = "UserName"  # Variable to Store the String "UserName"
print("The Statement is ")
print("'", str1, str3, str2, "'") # Printing the String
rep = input("\nEnter the Replacing String for 'UserName': ")
if len(rep) >= 3: # Checking the Condition for string length with min length of 3
    print("\nString can be Replaced")
    print("\nStatement Before Replacing")
    print(str1, str3, str2)
    print("\nStatement After Replacing")
    repl = str.replace(str3, str3, rep)  # Replacing Logic for the String
    print("'", str1, repl, str2, "'")
else:
    print("!!! String cannot be Replaced !!!")
