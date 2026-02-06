# print the first 3 letters of a string, Followed by ..., followed by the last 3 letters of a string

#initialize the string
# string = "Polytechnic"

# display the results
# print("%s...%s" % (string[0:3], string[len(string)-3:len(string)]))

## Question 2 
# Extract the dollars and cents from a floating point price
# typecast the user input as a float
#price = float(input("Enter a price: "))

# Compute dollars and cents
# Cast dollars and cents to integers
#dollars = int(price)
#cents = int((price - dollars) * 100 + 0.5)

# Display the results
# print(dollars, "Dollars",cents, "Cents")
#comment the above line
# uncomment the line below to use f-strings to display the results
#print(f"{dollars} Dollars {cents} Cents")

## Question 3
# Create a list. List Methods allow you to manipulate
names = ["Fritz"]
names.insert(1, "Anne")
names.insert(0, "Melina")
names.pop(2)
names.append("Jorge")
# Add the comand to display the contents of the names list
# print(sorted(names))

## Question 4
# create a dictionary of key:value pairs
contacts = {"Jenny": 8675309, "James": 5551212}
print(*contacts) #asterisk unpacks argument
print("Jennys number is", contacts["Jenny"])
brian = contacts.get("James") # get the value of James key and assign it to brian
print("Brian has a new number:", brian)