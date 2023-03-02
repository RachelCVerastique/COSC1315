#------------------------------------------------------
#Programmer:    Rachel Verastique
#Course:        COSC 1315Section 001
#Semester:      Spring 2023
#Assignment #:  A05a
#Due Date:      March 5, 2023
#------------------------------------------------------

# main function
def main():
    # Prompt for 5 test scores
    tS1 = int(input("Enter test score 1: "))
    tS2 = int(input("Enter test score 2: "))
    tS3 = int(input("Enter test score 3: "))
    tS4 = int(input("Enter test score 4: "))
    tS5 = int(input("Enter test score 5: "))

    # Calculate average of test scores
    def calcAverage(tS1, tS2, tS3, tS4, tS5):
        averageScore = (tS1 + tS2 + tS3 + tS4 + tS5) / 5
        return averageScore

    # Determine letter grade for the scores
    def determineGrade(testScore):

        if 100 >= testScore >= 90:
            return "A"
        elif 80 <= testScore <= 89:
            return "B"
        elif 70 <= testScore <= 79:
            return "C"
        elif 60 <= testScore <= 69:
            return "D"
        else:
            return "F"

    # Calling calcAverage function
    averageScore = calcAverage(tS1, tS2, tS3, tS4, tS5)

    # Print out all 5 test scores / average score and determine their letter grade
    # by calling determineGrade function
    print(f"\nTest Score\t \t\tLetter Grade")
    print(f"--------------------------------")
    print(f"Test Score 1: {tS1}\t \t {determineGrade(tS1)}")
    print(f"Test Score 2: {tS2}\t \t {determineGrade(tS2)}")
    print(f"Test Score 3: {tS3}\t \t {determineGrade(tS3)}")
    print(f"Test Score 4: {tS4}\t \t {determineGrade(tS4)}")
    print(f"Test Score 5: {tS5}\t \t {determineGrade(tS5)}")
    print(f"--------------------------------")
    print(f"\nAverage Score: {format(averageScore, '.2f')}\t {determineGrade(averageScore)}")

    print("\nThis program was coded by Rachel Verastique.")
    print("End of program.")


# Calling main function
main()

