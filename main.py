questions=("how many tables in this room ? ",
           "how many persons in this room ? ")
options=(("A.3","B.4","C.5"),
         ("A.9","B.8","C.2"))
answers=("B","C")
guesses=[]
question_num=0
score=0

for question in questions:
    print("-------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("enter your choice (A,B,C) : " ).upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print("correct")
    else:
        print("incorrect")
        print(f"{answers[question_num]} is the correct answer ")
    question_num+=1
print("----------------------------------")
print("             RESULT               ")
print("----------------------------------")
print("The correct answers are : ", end="")
for answer in answers:
    print(answer, end=" ")
print()
print("Your guesses are : ",end="")
for guess in guesses:
    print(guess,end=" ")
print()
score=int(score/len(questions)*100)
print(f"------> Your score is {score}%")