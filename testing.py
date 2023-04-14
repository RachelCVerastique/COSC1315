

def main():
    translation = ''
    keepLooping = 1

    while keepLooping != 0:

        # prompt user to input a sentence for translation
        sentence = input('Type a sentence you would like translated: ')

        words = sentence.split()

        for word in words:

            newWord = word[1:] + word[0] + "ay" + " "

            translation = translation + newWord

        print(translation)

        # set variable to exit while loop
        keepLooping = 0
        printGoodbye()


def printGoodbye():
    print("\nThis program was coded by Rachel Verastique.")
    print("End of program.")


main()
