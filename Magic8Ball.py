# Magic8Ball
# Adding a yes/no question to return an answer.
# Nikki Smith
# 11/05/2022

import random

print('What is your name?')   # ask them for their name
myName = input()

print('What is your yes/no question?')   # ask them for a yes/no question
myQuestion = input()

def getAnswer(answerNumber):
    if answerNumber == 1:
        return myName + ', It is certain!'
    elif answerNumber == 2:
        return myName + ', It is decidedly so!'
    elif answerNumber == 3:
        return myName + ', Yes!'
    elif answerNumber == 4:
        return myName + ', Reply hazy try again.'
    elif answerNumber == 5:
        return myName + ', Ask again later.'
    elif answerNumber == 6:
        return myName + ', Concentrate and ask again.'
    elif answerNumber == 7:
        return myName + ', My reply is no.'
    elif answerNumber == 8:
        return myName + ', Outlook not so good.'
    elif answerNumber == 9:
        return myName + ', Very doubtful!'
    elif answerNumber == 10:
        return myName + ', Not a chance!'
r = random.randint(1, 10)
fortune = getAnswer(r)
print(fortune)

# Python's two levels of scope are local and global.
# Local scope is the code block or the body of any Python function expression. It contains
# the names that you define inside the function.
# Global scope is the top-most scope in Python that contains all of the names that you define
# at the top level of the program.



