#------------------------------------------------------
#Programmer:    Rachel Verastique
#Course:        COSC 1315Section 001
#Semester:      Spring 2023
#Assignment #:  A07
#Due Date:      March 29, 2023
#------------------------------------------------------

def main():
    # variables to be used
    total = 0
    counter = 0
    keepLooping = 1

    # define print goodbye function
    # will display goodbye message for program
    def printGoodbye():
        print("\nThis program was coded by Rachel Verastique.")
        print("End of program.")

    # keeps looping as long as th
    while keepLooping != 0:
        try:
            # prompt user for input file name
            fileName = input('Enter file name: ')

            # open fileName for reading
            infile = open(fileName, 'r')

            # for loop to read the file and add up numbers in file
            for line in infile:
                counter = counter + 1
                number = int(line)
                print(number)
                total += number
            # close the file
            infile.close()

            # calculate average of numbers
            average = total / counter

            # display average of numbers in file
            print(f"\nAverage: {format(average, '.2f')}")

            # set variable to exit while loop
            keepLooping = 0
            printGoodbye()

        except IOError:
            print("\nAn error occurred while trying to read the file")
            print("Please enter the correct file name.\n")
        except ValueError:
            print("\nNon-numeric data found in the file")
            print("Please attempt to read file again.\n")
        except:
            print("\nAn error occured")
            print("Abort Mission")


# call main
main()



