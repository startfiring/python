# use ascii table to encode string
# use ord() to convert char to ascii code
# use chr() to convert ascii value to char

def get_password(word):
    result = ""
    for letter in word:
        if (ord(letter) >= 120 and ord(letter) < 123) or (ord(letter) >= 88 and ord(letter) < 91):
            letter = chr(ord(letter) - 23)
        elif (ord(letter) >= 97 and ord(letter) < 120) or (ord(letter) >= 56 and ord(letter) < 88):
            letter = chr(ord(letter) + 3)

        result += letter
    return result

input_word = input("enter a word: ")
print("The new password is " + get_password(input_word))

### optimized code

ASCII_A = 65
ASCII_Z = 90
ASCII_a = 97
ASCII_z = 122

ALPHABET_LENGTH = 26

def encode_decode( phrase,  shift,  encode):
    if encode:
        string_return = ""
        for _char in phrase:

            ascii_code = ord (_char)

            if ((ascii_code >=  ASCII_A) and (ascii_code <=  ASCII_Z)) or ((ascii_code >=  ASCII_a) and (ascii_code <=  ASCII_z)):
                ascii_code += shift
                if  ((ascii_code > ASCII_Z) and (ascii_code <=  ASCII_Z + shift)) or ((ascii_code > ASCII_z) and (ascii_code <=  ASCII_z + shift)):
                    ascii_code = ascii_code - ALPHABET_LENGTH
                string_return += chr(ascii_code)
            else:
                string_return += _char
        
        return string_return
    else:
        string_return = ""
        for _char in phrase:

            ascii_code = ord (_char)

            if ((ascii_code >=  ASCII_A) and (ascii_code <=  ASCII_Z)) or ((ascii_code >=  ASCII_a) and (ascii_code <=  ASCII_z)):
                ascii_code -= shift
                if  ((ascii_code < ASCII_A) and (ascii_code <=  ASCII_A - shift)) or ((ascii_code < ASCII_a) and (ascii_code <=  ASCII_a + shift)):
                    ascii_code = ascii_code + ALPHABET_LENGTH
                string_return += chr(ascii_code)
            else:
                string_return += _char
        
        return string_return

orignal_phrase = "this is a sample 123 abc !@#"
print(orignal_phrase)

encode_phrase = encode_decode(orignal_phrase, 4, True)
print(encode_phrase)

decode_phrase = encode_decode(encode_phrase, 4, False)
print(decode_phrase)


