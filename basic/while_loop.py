
i = 1
while i <= 5:
    print(i)
    i = i + 1

print("down with loop")

secret_word = "John"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while (guess != secret_word) and (not(out_of_guesses)):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You win!")
    