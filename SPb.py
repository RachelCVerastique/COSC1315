#------------------------------------------------------
#Programmer:    Rachel Verastique
#Course:        COSC 1315Section 001
#Semester:      Spring 2023
#Assignment #:  SPb
#Due Date:      April 19, 2023
#------------------------------------------------------

def main():
    # Define variable and accumulator
    translation = ''
    keepLooping = 1

    while keepLooping != 0:

        # prompt user to input a sentence for translation
        sentence = input('Type a sentence you would like translated: ')

        # splits sentence into individual words to
        # be looped through
        words = sentence.split()

        # Loop through individual words, sends first letter of each
        # word to the end of the word and adds ay and a space at the end.
        # printed in all caps
        for word in words:

            newWord = word[1:] + word[0] + "ay" + " "

            translation = translation + newWord.upper()

        print(translation)

        # set variable to exit while loop
        keepLooping = 0
        # call printGoodbye function
        printGoodbye()


# define print goodbye function
# will display goodbye message for program
def printGoodbye():
    print("\nThis program was coded by Rachel Verastique.")
    print("End of program.")


# Call main function
main()
