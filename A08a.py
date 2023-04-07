#------------------------------------------------------
#Programmer:    Rachel Verastique
#Course:        COSC 1315Section 001
#Semester:      Spring 2023
#Assignment #:  A08a
#Due Date:      April 12, 2023
#------------------------------------------------------

# define summerStats that calculates
# total rainfall and average rainfall
# for summer months only
def summerStats(months, monthlyRain):
    summerMonths = months[5:8]
    summerRain = monthlyRain[5:8]
    print(f"Summer months: {summerMonths}")
    print(f"Summer rain: {summerRain}")

    # calculate total rainfall for summer months and print
    total = sum(summerRain)
    print(f"Total rainfall for summer months: {format(total, '.2f')}")

    # calculate average summer rainfall
    average = total / len(summerRain)

    # return average for summer rainfall
    return average


# define endProgram
def endProgram():
    print("\nThis program was coded by Rachel Verastique.")
    print("End of program.")

# This program calculates rain fall for the year


# define main function
def main():
    # create list of months
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]

    # create a list for monthly rain values
    monthlyRain = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                   0.0, 0.0, 0.0]

    # prompt user to input values for rain fall each month
    num = len(months)

    for i in range(num):
        monthlyRain[i] = float(input(f"enter the rainfall for {months[i]} "))

    # calculate total amount of rainfall
    total = sum(monthlyRain)

    # calculate the average rainfall
    average = total / num

    # calculate max of rainfall
    maxRain = max(monthlyRain)

    # calculate min rainfall
    minRain = min(monthlyRain)

    # Get index of the month with max rainfall
    maxMonth = monthlyRain.index(maxRain)

    # get the index of the month with min rainfall
    minMonth = monthlyRain.index(minRain)

    # Print out results
    print(f"Total rainfall: {format(total, '.2f')}")
    print(f"Average rainfall: {format(average, '.2f')}")
    print(f"Max. rainfall in: {months[maxMonth]} at {monthlyRain[maxMonth]} inches.")
    print(f"Min. rainfall in: {months[minMonth]} at {monthlyRain[minMonth]} inches.")


    # call on 'summerStats' function that cuts out all months but summer months
    averageSumRain = summerStats(months, monthlyRain)
    print(f"Average rainfall during summer months: {format(averageSumRain, '.2f')}")

    # call endProgram function
    endProgram()


main()




