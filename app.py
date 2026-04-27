# asks user for how much they spent
spent = input("How much did you spend this week on groceries?\n")

# error handling in case the user inputs bad data.
try:
        # convert values to decimal and ask the user for how much they earned.
        spent  = float(spent)
        earned = input("How much did you earn this week from working?\n")
        earned = float(earned)
except ValueError:
        # handle error if it occurs. Let the user know what they must do.``
        print("Please enter a valid dollar cent amount")
        exit()

# calculate how much the user can still spend or if they are in debt.
amount_left = earned - spent

# handle 3 cases. If the user spent too much, exactly their earnings, or less.
# prints message for each of the 3 cases and printf for printing with 2 decimal places.
if amount_left < 0:
        print (f"You have spent ${-amount_left:.2f} more than you have earned this week.")
elif amount_left == 0:
        print ("You have spent exactly what you have earned this week.")
else:
        print (f"You still have ${amount_left:.2f} to spend for the week or to put in savings!")

