age = input('Enter your age:')
if int(age) >= 18:
    print("You're eligible to vote.")
    

age = input('Enter your age:')
if int(age) >= 18:
    print("You're eligible to vote.")
    print("Let's go and vote.")


age = input('Enter your age:')
if int(age) >= 18:
    print("You're eligible to vote.")
print("Let's go and vote.")


'''
if condition:
    if-block;
else:
    else-block;
'''

age = input('Enter your age:')
if int(age) >= 18:
    print("You're eligible to vote.")
else:
    print("You're not eligible to vote.")


'''
if if-condition:
    if-block
elif elif-condition1:
    elif-block1
elif elif-condition2:
    elif-block2
...
else:
    else-block
'''

age = input('Enter your age:')

# convert the string to int
your_age = int(age)

# determine the ticket price
if your_age < 5:
    ticket_price = 5
elif your_age < 16:
    ticket_price = 10
else:
    ticket_price = 18

# show the ticket price
print(f"You'll pay ${ticket_price} for the ticket")



# Ternary Operator
age = 18;

if int(age) >= 18:
    ticket_price = 20
else:
    ticket_price = 5

age = input('Enter your age:')

# value_if_true if condition else value_if_false
ticket_price = 20 if int(age) >= 18 else 5

print(f"The ticket price is {ticket_price}")


# for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


string = "Python"
for char in string:
    print(char)


for number in range(1, 6):
    print(number)


#range(start, stop, step)

for index in range(0, 11, 2):
    print(index)


# while loop
max = 5
counter = 0

while counter < max:
    print(counter)
    counter += 1


command = ''

while command.lower() != 'quit':
    command = input('>')
    print(f"Echo: {command}")


#Python pass

# The pass statement is a statement that does nothing. 
# It’s just a placeholder for the code that you’ll write in the future.

counter = 1
max = 10
if counter <= max:
    counter += 1
else:
    pass

