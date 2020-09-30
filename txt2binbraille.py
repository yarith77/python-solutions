# incomplete
# only work with a-z, A-z, 1-9, space, some symbols

# pattern:
# 1 4
# 2 5
# 3 6
# binary pattern is 123456

s = input("Input: ")
braille_dec = {
    'a': 32, 'b': 48, 'c': 36, 'd': 38, 'e': 34, 'f': 52,
    'g': 54, 'h': 50, 'i': 20, 'j': 22, 'k': 40, 'l': 56,
    'm': 44, 'n': 46, 'o': 42, 'p': 60, 'q': 62, 'r': 58,
    's': 28, 't': 30, 'u': 41, 'v': 57, 'w': 23, 'x': 45,
    'y': 47, 'z': 43, '0': 22, '1': 32, '2': 48, '3': 36,
    '4': 38, '5': 34, '6': 52, '7': 54, '8': 50, '9': 20,
    ' ': 0, '.': 19, ',': 16, '?': 25, '!': 26, ':': 18, 
    ';': 24, "'": 8, '“': 11, '”': 25
}

translation = ''
for i in s:
    if i.isupper():
        translation += '000001'
        i = i.lower()
    translation += '{:06b} '.format(braille_dec[i])
print("Output:", translation, sep='\n')
