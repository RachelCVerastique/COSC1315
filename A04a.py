#------------------------------------------------------
#Programmer:    Rachel Verastique
#Course:        COSC 1315Section 001
#Semester:      Spring 2023
#Assignment #:  1a
#Due Date:      March 1, 2023
#------------------------------------------------------


ST_TAX_RATE = 0.05
CO_TAX_RATE = 0.025


def main():

    # Prompt for purchase amount
    purchase = float(input("Please enter the amount of a purchase: "))

    # calculate state tax
    stTax = ST_TAX_RATE * purchase

    # calculate county tax
    coTax = CO_TAX_RATE * purchase

    # call showSale function
    showSale(purchase, stTax, coTax)

    print("\nThis program was coded by Rachel Verastique.")
    print("End of program.")


def showSale(purchase, stTax, coTax):

    # calculate total tax
    totalTax = stTax + coTax

    # calculate total sale cost
    totalSale = purchase + totalTax

    # Print out all information regarding sale
    print(f"\nPurchase amount: ${format(purchase, '.2f')}")
    print(f"State tax: ${format(stTax, '.2f')}")
    print(f"County tax: ${format(coTax, '.2f')}")
    print(f"Total tax: ${format(totalTax, '.2f')}")
    print(f"Total sale: ${format(totalSale, '.2f')}")


main()












