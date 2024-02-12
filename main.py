morse_dictionary = {
    "A": "・—",
    "B": "—・・・",
    "C": "—・—・",
    "D": "—・・",
    "E": "・",
    "F": "・・—・",
    "G": "— —・",
    "H": "・・・・",
    "I": "・・",
    "J": "・— — —",
    "K": "—・—",
    "L": "・—・・",
    "M": "— —",
    "N": "—・",
    "O": "— — —",
    "P": "・— —・",
    "Q": "— —・ —",
    "R": "・—・",
    "S": "・・・",
    "T": "—",
    "U": "・・—",
    "V": "・・・—",
    "W": "・— —",
    "X": "—・・ —",
    "Y": "—・ — —",
    "Z": "— —・・",

}


def convert_to_morse(message):
    # split each word into an array
    words_array = message.split()

    morse_word_array = []
    # loop through each word
    for word in words_array:
        morse_word = ""
        # loop through each letter in word
        for letter in word:
            morse_letter = morse_dictionary[letter]
            morse_word += morse_letter + "  "
        morse_word_array.append(morse_word)

    return morse_word_array


if __name__ == "__main__":

    print("*** MorseCodeMaker ***")
    message_maker = True

    while message_maker:
        message_to_convert = input("Enter the message you would like converting to morse code or type QUIT:\n> ")

        if message_to_convert == 'QUIT':
            message_maker = False
        else:
            morse_code = convert_to_morse(message_to_convert.upper())
            print(f'The message "{message_to_convert.capitalize()}" in morse code is:\n {morse_code}')
