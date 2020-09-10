# we will be guessing the word till we have the power

guess= ""
real_word = "Manu"
try_count = 0
total_guesses = 3
have_count = True


while guess != real_word and have_count:
    guess = input("Guess the name: ")
    try_count=try_count+1
    if try_count>=total_guesses:
        have_count = False

if(have_count):
    print("You gussed it Right")
else:
    print("Ahh! man try again")


    
