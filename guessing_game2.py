# This is a guessing game program, where an user have to keep on guessing the seceret word, using while loop till the user can't guess it correctly, it will keep on guessing. And added the guess count.

secret_word = "riddhi"
guess_word = ""
guess_count = 0
guess_limit = 3
out_of_guess = False
while guess_word != secret_word and not(out_of_guess) :
    if guess_count < guess_limit :
        guess_word = input("Please enter any guess_word : ")
        guess_count += 1
    else :
        out_of_guess = True
if out_of_guess :
    print("Sorry ! Out of guess...You Lose!! ") 
else :
    print("Congrulations !!! You Won..")