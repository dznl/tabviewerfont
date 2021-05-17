digit_to_glyph = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    'T': 'T',
    'E': 'E'
}


def base10_to_base12digit(base10):
    if base10 == '10':
        return 'T'
    if base10 == '11':
        return 'E'
    return str(base10)


def digitstring_to_glyphstring(digits):
    return ' '.join(digit_to_glyph[d] for d in digits)


print('@digit = [zero one two three four five six seven eight nine];')

for glyph in digit_to_glyph.values():
    print(f'lookup to_{glyph} {{ substitute @digit by {glyph}; }} to_{glyph};')

print('''
feature calt {
''')

for n10 in range(10, 100):
    s10 = str(n10)
    msd10 = digit_to_glyph[s10[0]]
    lsd10 = digit_to_glyph[s10[1]]
    msd12 = digit_to_glyph[base10_to_base12digit(str(n10 // 12))]
    lsd12 = digit_to_glyph[base10_to_base12digit(str(n10 % 12))]

    print(f"  substitute {msd10}' lookup to_{msd12} {lsd10}' lookup to_{lsd12} ;")

print('''
} calt;
''')
