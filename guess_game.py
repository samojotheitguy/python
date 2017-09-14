import random

print('**************Guess The Programming Language Game**************\n')  # title of the game

Plangs = ("python", "php", "javascript", "c", "perl", "c++", "java", "ruby", "c#", "visual basic",
          "fortran")  # this will be the array word for the guess game

answer = random.choice(Plangs)  # this will randomly pick the word from an array

correct = answer  # If the has been picked the word will into a new variable

rumble = ""  # creating a new variable

while answer:  # check if answer is true
    position = random.randrange(len(answer))  # get the range of the word
    rumble += answer[position]  # then rumble the word of choice
    answer = answer[:position] + answer[(position + 1):]  # rearrange the rumble words

print("The Word Is:", rumble)  # display the jumble word

guess = input("Guess This Programming Language:")  # create a input for answering the guess word
guess = guess.lower()  # lowercase the jumble word

while (guess != correct) or (guess == ""):  # check if the given answer is incorrect
    print("That is not the correct answer")
    print("\nThe Word Is:", rumble)
    guess = input("Guess This Programming Language:")
    guess = guess.lower()

if guess == correct:  # check if the answer is correct
    print("\nCongratulation You Win!")
    input("\n\n Press enter to exit")