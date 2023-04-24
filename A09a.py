#------------------------------------------------------
#Programmer:    Rachel Verastique
#Course:        COSC 1315Section 001
#Semester:      Spring 2023
#Assignment #:  A09a
#Due Date:      April 26, 2023
#------------------------------------------------------

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