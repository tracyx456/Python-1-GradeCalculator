# Get input scores from keyboard
iLabCompleted = int(input("Enter the number of labs completed: "))
iQuizzesComplete = int(input("Enter the number of quizzes completed: "))
iAssignment1 = int(input("Enter grade for Assignment 1: "))
iAssignment2 = int(input("Enter grade for Assignment 2: "))
iAssignment3 = int(input("Enter grade for Assignment 3: "))
iAssignment4 = int(input("Enter grade for Assignment 4: "))
iMidterm1 = int(input("Enter grade for Midterm 1: "))
iMidterm2 = int(input("Enter grade for Midterm 2: "))
iFinalExam = int(input("Enter grade for Final Exam: "))
iPreparation = int(input("Enter grade for Midterms and Final Preparation: "))

# Adjust lab and quiz completed up to 6
if iLabCompleted > 6:
    iLabCompleted = 6
if iQuizzesComplete > 6:
    iQuizzesComplete = 6

# Calculate grade as float data type
fGrade = (iLabCompleted / 6) * 0.2 * 100 + (iQuizzesComplete / 6) * 0.15 * 100 + ((iAssignment1 + iAssignment2 + iAssignment3 + iAssignment4) / 4) * 0.16 + ((iMidterm1 + iMidterm2) / 2) * 0.25 + iFinalExam * 0.18 + iPreparation * 0.06

# Output rounded grade
print("Your grade is:", round(fGrade))
