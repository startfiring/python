
def get_password(word):
    password = ""
    for letter in word:
        list_letter = {
            "a": "d",
            "b": "e",
            "c": "f",
            "d": "g",
            "e": "h",
            "f": "i",
            "g": "j",
            "h": "k",
            "i": "l",
            "j": "m",
            "k": "n",
            "l": "o",
            "m": "p",
            "n": "q",
            "o": "r",
            "p": "s",
            "q": "t",
            "r": "u",
            "s": "v",
            "t": "w",
            "u": "x",
            "v": "y",
            "w": "z",
            "x": "a",
            "y": "b",
            "z": "c",


        }
        if letter in list_letter:
            letter = letter
        password += letter
    return password

input_word = input("enter a word: ")
print("The new password is " + input_word)


