from Main import morse_code
def coder(text):
    encoded = ''
    for char in text.upper():
        if char in morse_code:
            encoded += morse_code[char] + " "
    return encoded

def decoder(morsecode):
    decoded = ''
    morsecode_list = morsecode.split(' ')
    for item in morsecode_list:
        if item in morse_code.values():
            for key, value in morse_code.items():
                if item == value:
                    decoded += key
    return decoded