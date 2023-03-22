#------------------------------------------------------
#Programmer:    Rachel Verastique
#Course:        COSC 1315Section 001
#Semester:      Spring 2023
#Assignment #:  A06b
#Due Date:      March 22, 2023
#------------------------------------------------------
def main():
    # variables
    total = 0

    # Prompt for name of file to open
    fileName = input("Enter file name you would like to open: ")

    # Open file to read
    infile = open(fileName, 'r')

    # Create new file for writing
    nFile = open("newFile.txt", 'w')

    # for loop to read file content
    for line in infile:
        number = int(line)
        print(number)
        total += number

        # If number is even, double it. If number is odd, triple it.
        if number % 2 == 0:
            number = number * 2
        else:
            number = number * 3

        # write new doubled and tripled values to
        # new file newFile.txt
        nFile.write(str(f'{number} \n'))

    # display total of numbers from the original file
    print("Total: ", total)

    # close files
    infile.close()
    nFile.close()

    # open newFile.txt for reading
    nFile = open("newFile.txt", 'r')
    print("\nNew file: ")
    total = 0

    # for loop to read and print file content
    for line in nFile:
        number = int(line)
        print(number)
        total += number

    # display total of numbers in newly created file
    print("Total", total)

    print("\nThis program was coded by Rachel Verastique.")
    print("End of program.")

if __name__ == '__main__':
