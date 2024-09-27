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

fGrade = (iLabCompleted / 6) * 0.2 + (iQuizzesComplete / 6) * 0.15 + ((iAssignment1 + iAssignment2 + iAssignment3 + iAssignment4) / 4) * 0.16 + ((iMidterm1 + iMidterm2) / 2) * 0.25 + iFinalExam * 0.18 + iPreparation * 0.06

print("Your grade is:", round(fGrade))
