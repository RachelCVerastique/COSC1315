#------------------------------------------------------
#Programmer:    Rachel Verastique
#Course:        COSC 1315 Section 001
#Semester:      Spring 2023
#Assignment #:  A03a
#Due Date:      February 22,2023
#------------------------------------------------------

amountSpent = 1.00
totalExpenses = 0.00

# Asking for monthly budget
monthlyBudget = float(input("Enter monthly budget: "))

# Ask for cost of expenses
while amountSpent != 0:
    amountSpent = float(input("Please enter an expense or Enter 0 to exit"))
    totalExpenses = totalExpenses + amountSpent


# Print out monthly budget and amount spent
print(f"\nYour monthly budget is: ${format(monthlyBudget, '.2f')}")
print(f"\nYour total expenses for the month is: ${format(totalExpenses, '.2f')}")


# inform of over budget/ under/ exact budget
# user went over budget
if totalExpenses > monthlyBudget:
    difference = totalExpenses - monthlyBudget
    print(f"\nYou have gone over budget for the month by ${format(difference,'.2f')}. Please try harder next month.")
# User was under budget
elif totalExpenses < monthlyBudget:
    difference = monthlyBudget - totalExpenses
    print(f"\nYou're under your monthly budget by ${format(difference,'.2f')}, Good job! Keep up the good work!")
# User spent exactly their budget amount
else:
    print(f"\nYou spent exactly your budget amount of ${monthlyBudget}. Good work!")





print("\nThis program was coded by Rachel Verastique.")
print("End of program.")
