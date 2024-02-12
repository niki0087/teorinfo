from morse_code import morse_code
def coder(text):
    encoded = ''
    for char in text.upper():
        if char in morse_code:
            encoded += morse_code[char] + " "
    return encoded