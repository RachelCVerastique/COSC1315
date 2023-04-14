#------------------------------------------------------
#Programmer:    Rachel Verastique
#Course:        COSC 1315Section 001
#Semester:      Spring 2023
#Assignment #:  SPa
#Due Date:      April 19, 2023
#------------------------------------------------------

def main():
    # set variables / accumulators
    upperC = 0
    lowerC = 0
    digits = 0
    wSpace = 0
    keepLooping = 1

    # keep looping as long as there is an exception that has been raised
    while keepLooping != 0:
        try:
            # prompt user for input file name
            fileName = input('Enter file name: ');

            # open fileName for reading
            infile = open(fileName, 'r');

            # read data from input file
            data = infile.read();

            # for loop to read the file
            for char in data:
                if char.isupper():
                    upperC += 1

                if char.islower():
                    lowerC += 1

                if char.isdigit():
                    digits += 1

                if char.isspace():
                    wSpace +=1

            # close the file
            infile.close();

            # Display results
            print(f'In {fileName} there are:');
            print(f'{upperC} Capital letters,');
            print(f'{lowerC} Lowercase letters,');
            print(f'{digits} Numbers,');
            print(f'and {wSpace} Spaces.');

            # variable to end loop
            keepLooping = 0

            # call printGoodbye function
            printGoodbye()

        except IOError:
            print("An error occured while trying to read the file.")
            print("Please enter the correct file name.")

 # define print goodbye function
 # will display goodbye message for program
 def printGoodbye():
     print("\nThis program was coded by Rachel Verastique.")
     print("End of program.")


# call main function
main()









