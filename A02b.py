#------------------------------------------------------
#Programmer:    Rachel Verastique
#Course:        COSC 1315 Section 001
#Semester:      Spring 2023
#Assignment #:  A02b
#Due Date:      February 8,2023
#------------------------------------------------------
# constants in program
SECONDS_IN_MIN = 60
SECONDS_IN_HOUR = 3600
SECONDS_IN_DAY = 86400

# initialize variables
hours = 0
days = 0
minutes = 0

# Prompt user to enter number of seconds
numOfSeconds = int(input("Enter a number of seconds: "))

# Calculate number of days from entered seconds
if numOfSeconds >= SECONDS_IN_DAY:
    days = numOfSeconds // SECONDS_IN_DAY
    dayRemainder = numOfSeconds % SECONDS_IN_DAY

# calculate the number of hours from seconds
if numOfSeconds >= SECONDS_IN_HOUR:
    hours = numOfSeconds // SECONDS_IN_HOUR
    hourRemainder = numOfSeconds % SECONDS_IN_HOUR

# calculate number of minutes from seconds
if numOfSeconds >= SECONDS_IN_MIN:
    minutes = numOfSeconds // SECONDS_IN_MIN
    minRemainder = numOfSeconds % SECONDS_IN_MIN

# print out number of days, hours, minutes and seconds
if minutes == 0:
    print("The number of seconds entered is less than one minute:", numOfSeconds, "seconds.")
else:
    print(numOfSeconds, "seconds is equivalent to:", minutes, "minute(s) and ", minRemainder, "seconds.")

if hours != 0:
    print(hours, "hour(s) and", hourRemainder, "seconds.")

if days != 0:
    print(days, "day(s) and", dayRemainder, "seconds.")


print("\nThis program was coded by Rachel Verastique.")
print("End of program.")


#
# # Determine the number of seconds
#
# if numOfSeconds >= SECONDS_IN_MIN and numOfSeconds < SECONDS_IN_HOUR:
#     print("\nThe amount of seconds entered is equivalent to: ", format(secToMins, '.0f'),
#           "Minutes and ", secRemain, "seconds.")
# elif numOfSeconds >= SECONDS_IN_HOUR and numOfSeconds < SECONDS_IN_DAY:
#     print("\nThe amount of seconds entered is equivalent to: ", format(secToHours, '.0f'),
#           "Hours and ", format(secToMins, '.0f'), "Minutes and ", secRemain, "seconds.")
# else:
#     print("\nThe amount of seconds entered is equivalent to: ", format(secToDays, '.0f'),
#           "Days and ", format((numOfSeconds % SECONDS_IN_DAY) /, '.0f'), "Hours and ", format(secToMins, '.0f'),
#           "Minutes and ", secRemain, "seconds.")

# Calculate conversion seconds to minutes, seconds to hours, seconds to days and remaining seconds
# secToMins = numOfSeconds / SECONDS_IN_MIN
# secToHours = numOfSeconds / SECONDS_IN_HOUR
# secToDays = numOfSeconds / SECONDS_IN_DAY

