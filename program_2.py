# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247 

# + 129

#Author: Sam Gaines
#Date: 2/19/2026
#Title: Math Quiz
import random
def math_quiz():
    #chooses a number
    num1= random.radiant(1,1000)
    num2= random.radiant(1,1000)
    #asks user to add the two numbers 
    print(f"What is {num1}+{num2}?")
    user_answer= int(input("Please enter your answer"))
    correct_answer= num1 + num2
    #Congratulates user if correct, corrects user if wrong 
    if user_answer == correct_answer:
        print("Congratulations! You got the correct answer!")
    else:
        print(f"Sorry, the correct answer is {correct_answer} ")

if __name__ == "__main__":
    math_quiz()

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.
