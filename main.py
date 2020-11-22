
import winsound

MORSE_CODE = {
    "a":".-", 
    "b":"---.",
}

def beep(duration):
    frequency = 200  # Set Frequency To 2500 Hertz
    # duration = 3000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)


def long_beep():
    beep(3000)


def short_beep():
    beep(1000)


# define all letters(data struture)

def play_sound_for_letter(letter):
    print(letter)
     # define all letters
     # look up letters based on input
     # loop over each character in the value string
     # translate dots and dashes to long and short sounds

# returns single letter (eg: a, b, c) for a given pattern (eg: .-, ---.)
def get_letter_for_pattern(pattern):
    print(pattern)


# long_beep()
short_beep()