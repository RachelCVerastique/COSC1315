#------------------------------------------------------
#Programmer:    Rachel Verastique
#Course:        COSC 1315Section 001
#Semester:      Spring 2023
#Assignment #:  A10
#Due Date:      May 3, 2023
#------------------------------------------------------

# define IO class

class IO:
    # define init method
    def __init__(self):
        self.__petName = ""
        self.__petType = ""
        self.__petAge = 0

    # define mutator methods
    def promptName(self):
        self.__petName = input("Enter the pets name: ")
        return self.__petName

    def promptType(self):
        self.__petType = input("Enter the type of animal: ")
        return self.__petType

    def promptAge(self):
        self.__petAge = input("Enter pets age: ")
        return self.__petAge


    # define printGoodbye
    def printGoodbye(self):
        print("\nThis program was coded by Rachel Verastique.")
        print("End of program.")