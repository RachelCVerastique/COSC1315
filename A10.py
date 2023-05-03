#------------------------------------------------------
#Programmer:    Rachel Verastique
#Course:        COSC 1315Section 001
#Semester:      Spring 2023
#Assignment #:  A10
#Due Date:      May 3, 2023
#------------------------------------------------------

# import classes
import mypet
import myIO

def main():
    # declare local variables to show what data types they are
    petName = ""
    petType = ""
    petAge = 0

    # instantiate an object from the class IO
    interact = myIO.IO()

    # prompt user for name, type and age of pet.
    petName = interact.promptName()
    petType = interact.promptType()
    petAge = interact.promptAge()

    # instantiate object from class pet
    aPet = mypet.Pet(petName, petType, petAge)

    # print out object info
    print("Here is the data that you entered: ")
    print("Pet name: ", aPet.getName())
    print("Pet type: ", aPet.getAnimalType())
    print("Pet age: ", aPet.getAge())

    # prompt user to enter new data about pet
    print("Now enter new values for the pet:", aPet.getName())
    petName = interact.promptName()
    petType = interact.promptType()
    petAge = interact.promptAge()

    # invoke mutator methods to update pets info
    aPet.setName(petName)
    aPet.setAnimalType(petType)
    aPet.setAge(petAge)


    # print out info about object
    print("Here is the new data you entered")
    print("Pet name: ", aPet.getName())
    print("Pet type: ", aPet.getAnimalType())
    print("Pet age: ", aPet.getAge())

    # call printGoodbye
    interact.printGoodbye()


# call main function
main()

