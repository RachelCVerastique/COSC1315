#------------------------------------------------------
#Programmer:    Rachel Verastique
#Course:        COSC 1315Section 001
#Semester:      Spring 2023
#Assignment #:  A04b
#Due Date:      March 1, 2023
#------------------------------------------------------

# Constants
A_SEATS = 20
B_SEATS = 15
C_SEATS = 10

def main():
    # Prompt asking for how many tickets of each sold
    aTicketsSold = int(input("How many Class A tickers were sold? "))
    bTicketsSold = int(input("How many Class B tickers were sold? "))
    cTicketsSold = int(input("How many Class C tickers were sold? "))

    # Calculating income for each ticket class
    aIncome = A_SEATS * aTicketsSold
    bIncome = B_SEATS * bTicketsSold
    cIncome = C_SEATS * cTicketsSold

    # calculating incomes and printing out info
    def showIncome(aIncome, bIncome, cIncome):
        # Calculating total income of all ticket classes combined
        totalIncome = aIncome + bIncome + cIncome
        # Calculating number of total tickets sold
        totalTicketsSold = aTicketsSold + bTicketsSold + cTicketsSold

        # Printing out info on tickets and income
        print(f"\nNumber of Class A tickets sold: {aTicketsSold} "
              f"\nTotal Class A tickets income: ${format(aIncome, '.2f')}")
        print(f"\nNumber of Class B tickets sold: {bTicketsSold} "
              f"\nTotal Class B tickets income: ${format(bIncome, '.2f')}")
        print(f"\nNumber of Class C tickets sold: {cTicketsSold}"
              f"\nTotal Class C tickets income: $", format(cIncome, '.2f'), sep='')

        print(f"\nTotal number of tickets sold: {totalTicketsSold}")
        print(f"Total income from all tickets sold: ${format(totalIncome, '.2f')}")
    # determining which ticket class sold the most
    def mostTickets(aTicketsSold, bTicketsSold, cTicketsSold):
        if aTicketsSold > bTicketsSold and aTicketsSold > cTicketsSold:
            print(f"\nClass A sold the most tickets")

        elif bTicketsSold > aTicketsSold and bTicketsSold > cTicketsSold:
            print(f"\nClass B sold the most tickets")

        elif cTicketsSold > aTicketsSold and cTicketsSold > bTicketsSold:
            print(f"\nClass C sold the most tickets")

        else:
            if aTicketsSold == bTicketsSold == cTicketsSold:
                print(f"\nClass A, Class B and Class C sold an equal amount of tickets: {aTicketsSold}")

            elif aTicketsSold == bTicketsSold:
                print(f"\nClass A and Class B tickets sold the most: {bTicketsSold}")

            elif aTicketsSold == cTicketsSold:
                print(f"\nClass A and Class C tickets sold the most: {aTicketsSold}")

            elif bTicketsSold == cTicketsSold:
                print(f"\nClass B and Class C tickets sold the most: {cTicketsSold}")

    # calling showIncome function
    showIncome(aIncome, bIncome, cIncome)

    # calling mostTickets function
    mostTickets(aTicketsSold, bTicketsSold, cTicketsSold)

    print("\nThis program was coded by Rachel Verastique.")
    print("End of program.")

# calling main function
main()