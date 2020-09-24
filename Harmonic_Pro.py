n= int(input("enter the value of n"))  #initialize the value
s=0.0
for i in range(1, n + 1):   #Using for loop to determine the value of git
        s = s + 1 / i ;     #store the value of each iteration
print("Sum is", round(s,3))  #using round function to give out put by round off