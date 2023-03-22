#------------------------------------------------------
#Programmer:    Rachel Verastique
#Course:        COSC 1315Section 001
#Semester:      Spring 2023
#Assignment #:  A06a
#Due Date:      March 8, 2023
#------------------------------------------------------

def main():
    # Variable
    counter = 0

    # prompt user for file they want to open
    fileName = input("Enter the name of the file you would like to open: ")

    # open the file user requested
    file = open('{fileName, r')

    # read file after opening
    for line in file:
        counter += 1
        print(counter, end='')
        print(":", end=' ')

        # strip new line character
        line = line.rstrip('\n')
        print(line)

    # close files
    file.close()

    print("\nThis program was coded by Rachel Verastique.")
    print("End of program.")


# Call main
if __name__ == '__main__':
    main()
