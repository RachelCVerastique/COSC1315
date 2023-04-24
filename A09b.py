#------------------------------------------------------
#Programmer:    Rachel Verastique
#Course:        COSC 1315Section 001
#Semester:      Spring 2023
#Assignment #:  A09b
#Due Date:      April 26, 2023
#------------------------------------------------------

def main():
    # declare variable and empty dictionary
    keepLooping = 1
    counter = { }

    # keep looping as long as an exception is raised
    while keepLooping != 0:
        try:
            # Prompt user for input file name
            inputName = input("Enter the name of the input file: ")
            inputFile = open(inputName, 'r')

            # read data in file
            text = inputFile.read()

            # divide input into individual words
            # and initialize into a list
            words = text.split()

            # add each word to dictionary in counter
            uniqueWords = set(words)

            # go through dictionary of unique words
            # set current frequency to zero
            for word in uniqueWords:
                counter[word] = 0

            # increase dictionaries counter with each word
            # in "words" list
            for item in words:
                counter[item] += 1

            # display results
            print(format("word", '15'), "\t",
                  format("occurrences", '15'))
            print("-------------------------------------")

            #print out words and their frequencies
            # as long there are words in dictionary counter
            while len(counter) > 0:
                # selects word at random and removes
                pair = counter.popitem()
                print(format(pair[0], '15'),
                      format(pair[1], '15'))

            # exit while loop
            keepLooping = 0

        except IOError:
            print("An error occured while trying to read the file.")
            print("Please enter the correct file name.")

    # call printGoodbye function
    printGoodbye()

# define print goodbye function
# will display goodbye message for program
def printGoodbye():
    print("\nThis program was coded by Rachel Verastique.")
    print("End of program.")


# call main function
main()
