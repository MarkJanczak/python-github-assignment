spent       = input("How much did you spend this week on groceries?\n")

try:
        spent  = float(spent)
        earned = input("How much did you earn this week from working?\n")
        earned = float(earned)
except ValueError:
        print("Please enter a valid dollar cent amount")
        exit()

amount_left = earned - spent
if amount_left < 0:
        print (f"You have spent ${-amount_left:.2f} more than you have earned this week.")
elif amount_left == 0:
        print ("You have spent exactly what you have earned this week.")
else:
        print (f"You still have ${amount_left:.2f} to spend for the week or to put in savings!")

