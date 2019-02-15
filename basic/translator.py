
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            letter = "g"
        translation += letter
    return translation

input_phrase = input("enter a word: ")
print("translated to: " + translate(input_phrase))

