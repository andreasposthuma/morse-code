import winsound
MORSE_CODE = {
    "a":".-", 
    "b":"-...",
    "c":"-.-.",
    "d":"-..",
    "e":".",
    "f":"..-.",
    "g":"--.",
    "h":"....",
    "i":"..",
    "j":".---",
    "k":"-.-",
    "l":".-..",
    "m":"--",
    "n":"-.",
    "o":"---",
    "p":".--.",
    "q":"--.-",
    "r":".-.",
    "s":"...",
    "t":"-",
    "u":"..-",
    "v":"...-",
    "w":".--",
    "x":"-..-",
    "y":"-.--",
    "z":"--.."

}


def beep(duration):
    frequency = 200  # Set Frequency To 2500 Hertz
    winsound.Beep(frequency, duration)


def long_beep():
    beep(1500)


def short_beep():
    beep(500)


# define all letters(data struture)
def play_sound_for_letter(letter):
    for sound in letter:
        if sound != "":
            sound += MORSE_CODE[letter]

        else:
            sound += ""
    




     # define all letters
     # look up letters based on input
     # loop over each character in the value string
     # translate dots and dashes to long and short sounds

# returns single letter (eg: a, b, c) for a given pattern (eg: .-, ---.)
def get_letter_for_pattern(pattern):
    morse = ""
    for message in pattern:
        if message != "":
            morse += MORSE_CODE[pattern] + ""
        else:

            morse += ""



# long_beep()
# short_beep()
get_letter_for_pattern("h")
play_sound_for_letter