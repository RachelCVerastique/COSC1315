#------------------------------------------------------
#Programmer:    Rachel Verastique
#Course:        COSC 1315 Section 001
#Semester:      Spring 2023
#Assignment #:  A01b
#Due Date:      February 1,2023
#------------------------------------------------------

#Promt for the number of females
females = int(input("Enter number of females in the class: "))

# Prompt for the number of males
males = int(input("Enter number of males in the class: "))

# Calculate total of males and females in the class
totalClass = females + males

# Calculate the percentage of females in the class
femalePercentage = females / totalClass

# Calculate the percentage of males in the class
malePercentage = males / totalClass

# Print values for the total of class and percentages of males and females
# Format the numbers ( 2 numbers behind the decimal point)
print('\nTotal number of students in class: ', totalClass)
print("\nMales have a total of ", males, " students with a percentage of ", format(malePercentage, '.2f') + \
      " or", format(malePercentage * 100, '.2f'), "%" + \
      " of the class.")
print("\nFemales have a total of ", females, " students with a percentage of ", format(femalePercentage, '.2f') + \
      " or", format(femalePercentage * 100, '.2f'), "%" + \
      " of the class.")

print("\nThis program was coded by Rachel Verastique.")
print("End of program.")
