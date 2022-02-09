# This is a guessing game program, where an user have to keep on guessing the seceret word, using while loop till the user can't guess it correctly, it will keep on guessing.

seceret_word = "riddhi"
guess_word = "" # empty string right now

# using a while loop, user will keep on guessing, untill they guess correctly

while guess_word != seceret_word :
    guess_word = input("Please enter the guess_word : ") # ask user to input a seceret word
print("Congrulations !! You Win !") # if guesses the word correctly, then breakdown this loop and print a success message. 