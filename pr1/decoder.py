from pr1.main import morse_code
def decoder(morsecode):
    decoded = ''
    morsecode_list = morsecode.split(' ')
    for item in morsecode_list:
        if item in morse_code.values():
            for key, value in morse_code.items():
                if item == value:
                    decoded += key
    return decoded