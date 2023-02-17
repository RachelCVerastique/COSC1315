# Constants to be used in program
PENNY_VAL = 1
NICKEL_VAL = 5
DIME_VAL = 10
QUARTER_VAL = 25
PENNIES_IN_DOLLAR = 100

# Prompt user for the number of each coin
numPennies = int(input(" Enter the number of pennies: "))
numNickels = int(input(" Enter the number of nickels: "))
numDimes = int(input(" Enter the number of dimes: "))
numQuarters = int(input(" Enter the number of quarters: "))

# Calculate total of coins
totalCoinsVal = (PENNY_VAL * numPennies) + \
                (NICKEL_VAL * numNickels) + \
                (DIME_VAL * numDimes) + \
                (QUARTER_VAL * numQuarters)

# Calculate dollar value
totalDollars = totalCoinsVal / PENNIES_IN_DOLLAR


# Determine if user won game
if totalDollars == 1.0:
    print("Congratulations! You have won the Money Counting Game!")

# Determine if user was over a dollar and by how much
elif totalDollars > 1.0:
    print("\nYour total was over a dollar.")
    print(" Your amount was $", format(totalDollars, '.2f'))
    print("You were over by $", format(totalDollars - 1.0, '.2f'))


else:
    print("Your total was under a dollar.")
    print("Your amount was $", format(totalDollars, '.2f'))
    print("You were under by $", format(1.0 - totalDollars, '.2f'))

print("\nThis program was coded by Rachel Verastique.")
print("End of program.")
