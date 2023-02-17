#------------------------------------------------------
#Programmer:    Rachel Verastique
#Course:        COSC 1315Section 001
#Semester:      Spring 2023
#Assignment #:  1a
#Due Date:      Feburary 1, 2023
#------------------------------------------------------

# Create a 'constant' for the sales tax rate
TAX_RATE = 0.07

# Prompt the user for the price of each of the five items.
# Assume prices will be floating point numbers

item1 = float(input("Enter the price of item #1: "))
item2 = float(input("Enter the price of item #2: "))
item3 = float(input("Enter the price of item #3: "))
item4 = float(input("Enter the price of item #4: "))
item5 = float(input("Enter the price of item #5: "))

# Calculate subtotal for all 5 items.
subtotal = item1 + item2 + item3 + item4 + item5

# Calculate sales tax for 5 items
tax = subtotal * TAX_RATE

# Add calculated subtotal and calcualted tax for total
total = subtotal + tax

# Print values for the subtotal, tax and final total
# Format the numbers in a nice format (2 numbers behind the decimal point)
print ("\nSubtotal: $", format(subtotal, '.2f'))
print ("Sales tax: $", format(tax, '.2f'))
print ("Total: $", format(total, '.2f'))

print ("\nThis program was coded by Rachel Verastique.")
print ("End of program.")


