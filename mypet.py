#------------------------------------------------------
#Programmer:    Rachel Verastique
#Course:        COSC 1315Section 001
#Semester:      Spring 2023
#Assignment #:  A10
#Due Date:      May 3, 2023
#------------------------------------------------------

# Define pet class
class Pet:
    def __init__(self, inName, inaAnimalType,inAge):
        self.__name = inName
        self.__animalType = inaAnimalType
        self.__age = inAge

    # define mutator methods
    def setName(self, inName):
        self.__name = inName

    def setAnimalType(self, inAnimalType):
        self.__animalType = inAnimalType

    def setAge(self, inAge):
        self.__age = inAge

    # Define accessor methods
    def getName(self):
        return self.__name

    def getAnimalType(self):
        return self.__animalType

    def getAge(self):
        return self.__age



