
# Day 45 - Online Examination System

# Questions and answers
questions = [
    {
        "question": "1. Which language is used for Python programming?",
        "options": ["A. HTML", "B. Python", "C. CSS", "D. SQL"],
        "answer": "B"
    },
    {
        "question": "2. Which function is used to display output in Python?",
        "options": ["A. input()", "B. print()", "C. scan()", "D. display()"],
        "answer": "B"
    },
    {
        "question": "3. Which data type stores True or False?",
        "options": ["A. String", "B. Integer", "C. Boolean", "D. Float"],
        "answer": "C"
    },
    {
        "question": "4. Which keyword is used to define a function?",
        "options": ["A. function", "B. def", "C. fun", "D. define"],
        "answer": "B"
    },
    {
        "question": "5. Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. **"],
        "answer": "C"
    }
]

# Student information
name = input("Enter your name: ")

score = 0

print("\n===== ONLINE EXAMINATION SYSTEM =====")
print("Welcome,", name)
print("Answer the following questions.")
print("Enter A, B, C, or D.\n")

# Display questions
for question in questions:
    print(question["question"])

    for option in question["options"]:
        print(option)

    answer = input("Enter your answer: ").upper()

    if answer == question["answer"]:
        print("Correct Answer!\n")
        score += 1
    else:
        print("Wrong Answer!")
        print("Correct answer:", question["answer"], "\n")

# Calculate result
total = len(questions)
percentage = (score / total) * 100

print("===== EXAM RESULT =====")
print("Student Name:", name)
print("Total Questions:", total)
print("Correct Answers:", score)
print("Wrong Answers:", total - score)
print("Percentage:", percentage, "%")

if percentage >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")

print("\nThank you for attending the examination!")
