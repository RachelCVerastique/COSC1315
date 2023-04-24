#
#
# def main():
#     translation = ''
#     keepLooping = 1
#
#     while keepLooping != 0:
#
#         # prompt user to input a sentence for translation
#         sentence = input('Type a sentence you would like translated: ')
#
#         words = sentence.split()
#
#         for word in words:
#
#             newWord = word[1:] + word[0] + "ay" + " "
#
#             translation = translation + newWord
#
#         print(translation)
#
#         # set variable to exit while loop
#         keepLooping = 0
#         printGoodbye()
#
#
# def printGoodbye():
#     print("\nThis program was coded by Rachel Verastique.")
#     print("End of program.")
#
#
# main()


def main():
    # declare variables and dictionaries.
    courseInfo = {'CS101':' Room: 3004 \n Instructor: Haynes \n Time: 8:00 a.m. ',
                  'CS102':' Room: 4501 \n Instructor: Alvarado \n Time: 9:00 a.m. ',
                  'CS103':' Room: 6755 \n Instructor: Rich \n Time: 10:00 a.m. ',
                  'NT110':' Room: 1244 \n Instructor: Burke \n Time: 11:00 a.m. ',
                  'CM241':' Room: 1411 \n Instructor: Lee \n Time: 1:00 p.m. '}

    keepLooping = 1

    # keep looping as long as user wants to keep enter course numbers
    while keepLooping != 0:
        # prompt user for course number
        course = input("Enter course number: ")

        # convert course number to upper case
        course = course.upper()

        # if course does not exist
        if course not in courseInfo:
            print(course, "is an invalid course number")

        else:
            # print course info
            print(f"Course details for {course} are as follows:")
            print(f"{courseInfo[course]}")

        # Prompt to see if user would like to continue
        # Remove first character and convert to lower case
        answer = input("Would you like to continue? (yes/no)?")
        answer = answer[0:1]
        answer = answer.lower()

        # if user wants to stop
        if answer == "n":
            # exit while loop
            keepLooping = 0

    # call printGoodbye function
    printGoodbye()

# define print goodbye function
# will display goodbye message for program
def printGoodbye():
    print("\nThis program was coded by Rachel Verastique.")
    print("End of program.")

# call main function
main()

# def main():
#     # declare variables and dictionaries.
#     rooms = {"CS101":3004, "CS102":4501, "CS103":6755, "NT110":1244, "CM241":1411}
#
#     instructors = {"CS101":"Haynes", "CS102":"Alvarado", "CS103":"Rich", "NT110":"Burke", "CM241":"Lee"}
#
#     times = {"CS101":"8:00 a.m.", "CS102":"9:00 a.m.", "CS103":"10:00 a.m.", "NT110":"11:00 a.m.", "CM241":"1:00 p.m."}
#
#     keepLooping = 1
#
#     # keep looping as long as user wants to keep enter course numbers
#     while keepLooping != 0:
#         # prompt user for course number
#         course = input("Enter course number: ")
#
#         # convert course number to upper case
#         course = course.upper()
#
#         # if course does not exist
#         if course not in rooms:
#             print(course, "is an invalid course number")
#
#         else:
#             # print course info
#             print(f"Course details for {course}:")
#             print(f"Room: {rooms[course]}")
#             print(f"Instructor: {instructors[course]}")
#             print(f"Time: {times[course]}")
#
#         # Prompt to see if user would like to continue
#         # Remove first character and convert to lower case
#         answer = input("Would you like to continue? (yes/no)?")
#         answer = answer[0:1]
#         answer = answer.lower()
#
#         # if user wants to stop
#         if answer == "n":
#             # exit while loop
#             keepLooping = 0
#
#     # call printGoodbye function
#     printGoodbye()
#
# # define print goodbye function
# # will display goodbye message for program
# def printGoodbye():
#     print("\nThis program was coded by Rachel Verastique.")
#     print("End of program.")
#
# # call main function
# main()

