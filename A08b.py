#------------------------------------------------------
#Programmer:    Rachel Verastique
#Course:        COSC 1315Section 001
#Semester:      Spring 2023
#Assignment #:  A08b
#Due Date:      April 12, 2023
#------------------------------------------------------

# define main function
def main():
    # Local variables
    number = 3
    numList = [10, 7, 8, 5, 4, 6, 2, 3, 9, 1]

    # print out number
    print(f'The magic number is: {number}')

    #print number list
    print(f'Original list of numbers {numList}')

    # sort the list
    numList.sort()

    #print the sorted list
    print(f"Sorted original list of numbers: {numList}")

    # display the list of numbers that are larger
    #than the magic number
    print(f"List of numbers that are larger than {number}.")

    #call showLargerThanNum function (takes in number and list)
    newList = showLargerThanNum(number, numList)
    print(newList)

    #call the greaterthanthreedoubleit function
    # passing the newList as an argument
    origList = greaterThanThreeDoubleIt(newList)
    print(f"Original list of numbers that are larger than {number}")
    print(origList)
    print(f"New list of numbers that are larger than {number} that have been doubled: ")
    print(newList)

    # call endProgram function
    endProgram()


# define greaterthanthreedoubleit function
# it will accept one parameter newlist
def greaterThanThreeDoubleIt(newList):
    #declare an empty list
    oldList = []

    num = len(newList)

    #loop through values in the newList
    for i in range(num):
        oldList.append(newList[i])
        newList[i] = newList[i] * 2

   # return th eoriginal list
    return oldList


#define showLargerThankNum function
def showLargerThanNum(n, nList):
    #declare empty list
    lgerThanNLst = []

    # loop thought values in list
    for value in nList:
        # determine if val is greater than n
        # if so append val to new list
        if value > n:
            lgerThanNLst.append(value)

   # return new list
    return lgerThanNLst

# define endProgram functions that displays end program message
def endProgram():
    print("\nThis program was coded by Rachel Verastique.")
    print("End of program.")

# call main function
main()
