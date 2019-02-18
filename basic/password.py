
def get_password(word):
    password = ""
    for letter in word:
        if letter in "a":
            letter = "d"
        elif letter in "b":
            letter = "e"
        elif letter in "c":
            letter = "f"
        elif letter in "d":
            letter = "g"
        elif letter in "e":
            letter = "h"
        elif letter in "f":
            letter = "i"
        elif letter in "g":
            letter = "j"
        elif letter in "h":
            letter = "k"
        elif letter in "i":
            letter = "l"
        elif letter in "j":
            letter = "m"
        elif letter in "k":
            letter = "n"
        elif letter in "l":
            letter = "o"
        elif letter in "m":
            letter = "p"
        elif letter in "n":
            letter = "q"
        elif letter in "o":
            letter = "r"
        elif letter in "p":
            letter = "s"
        elif letter in "q":
            letter = "t"
        elif letter in "r":
            letter = "u"
        elif letter in "s":
            letter = "v"
        elif letter in "t":
            letter = "w"
        elif letter in "u":
            letter = "x"
        elif letter in "v":
            letter = "y"
        elif letter in "w":
            letter = "z"
        elif letter in "x":
            letter = "a"
        elif letter in "y":
            letter = "b"
        elif letter in "z":
            letter = "c"
        password += letter
    return password
        

input_word = input("enter a word: ")
print("The new password is " + get_password(input_word))


