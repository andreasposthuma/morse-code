import winsound

def beep(duration):
    frequency = 200  # Set Frequency To 2500 Hertz
    # duration = 3000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)


def long_beep():
    beep(3000)


def short_beep():
    beep(1000)


def get_sound_for_letter(letter):
    print(letter)


def get_sound_for_pattern(pattern):
    print(pattern)


long_beep()
short_beep()