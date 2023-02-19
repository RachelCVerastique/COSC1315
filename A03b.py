#------------------------------------------------------
#Programmer:    Rachel Verastique
#Course:        COSC 1315 Section 001
#Semester:      Spring 2023
#Assignment #:  A03b
#Due Date:      February 22,2023
#------------------------------------------------------

# variables in program
totalRainFall = 0.0
totalMonths = 0

# Prompt for amount of years that rainfall is being tracked
years = int(input("Enter the number of years: "))

# prompt for the amount of rain per month for every year
# the aYear is the name of the for loop
# in range pulls the inputted years from the years variable
for aYear in range(years):
    # for every iteration ( if input of 3 years it will iterate once for 3 years) it will print "For year aYear
    # " ranging from year 1 to year 3. The + 1 is due to the count starting at 0
    print(f"For year {aYear + 1} :")

# month is the name of the loop and its in a range of 12 ( it will iterate 12 times (for every year in the inputted
# years))   and it will print "enter thr amount of rain fall each time.
    for month in range(12):
        monthlyRainFall = float(input("Enter amount of rainfall for the month (in inches): "))
# shorthand for totalMonths = totalMonths +1
        totalMonths += 1
# shorthand for totalRainFall = totalRainFall + monthlyRainFall
        totalRainFall += monthlyRainFall

    # calculate average rainfall
averageRainfall = totalRainFall / totalMonths

# print out total for months, rain and average of monthly rain
print(f"\n  {totalMonths} months")
print(f"Total rainfall: {format(totalRainFall, '.2f')} inches")
print(f"Average monthly rainfall: {format(averageRainfall, '.2f')} inches")





print("\nThis program was coded by Rachel Verastique.")
print("End of program.")
