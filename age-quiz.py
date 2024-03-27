# This code will ask the user for their age
number = int(input("What is your age? ")) # allows the user to input 
if number > 100: # looks for an age less than 100
    print("Sorry, you're dead.") # prints out a response based on the user input if it was >100
elif number > 65:
    print("Enjoy your reitrement!")
elif number > 40:
    print("You're over the hill.")
elif number == 21:
    print("Congrats on your 21st!")
elif number < 13:
    print("You qualify for the kiddie discount.")
else:
    print("Age is but a number.")