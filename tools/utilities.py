

def get_response():
    resp = input()
    if len(resp)> 0:
        return resp[0].lower()
    else:
        return 'No Response'

def get_long_response():
    resp = input()
    return resp.lower()

def convert_chars_to_ints(string_input):
    s = ''
    alphabet = {'a':99, 'b':98, 'c':97, 'd':96, 'e':95, 'f':94, 'g':93, 'h':92, 'i':91, 'j':90, 'k':89, 'l':88, 'm':87,
                'n':86, 'o':85, 'p':84, 'q':83, 'r':82, 's':81, 't':80, 'u':79, 'v':78, 'w':77, 'x':76, 'y':75, 'z':74,
                ' ':100}
    for character in string_input:
        s += str(alphabet[character])
    try:
        i = int(s)
    except Exception as E:
        print(E)
    return i

def pad_string(string_input, num_characters, pad_character):
    l = len(string_input)
    if l >= num_characters:
        return string_input[0:num_characters]
    else:
        return string_input + pad_character * (num_characters - l)

