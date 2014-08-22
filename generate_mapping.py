import re
import sys
import collections

hiragana_katakana_re = re.compile(r"HIRAGANA|KATAKANA")
hiragana_katakana_letter_re = re.compile(r"^(HIRAGANA|KATAKANA) LETTER ([A-Z ]+)$")

def main(input_file, output_file):
    letters = collections.defaultdict(lambda: [None, None])
    pos_hiragana, pos_katakana = 0, 1

    with open(input_file) as file:
        for line in file:
            if not hiragana_katakana_re.search(line):
                continue
            code_point, name, _ = line.split(";", 2)
            match = hiragana_katakana_letter_re.match(name)
            if match:
                is_hiragana = (match.group(1) == "HIRAGANA")
                letter = match.group(2)

                pos = pos_hiragana if is_hiragana else pos_katakana
                character = unichr(int(code_point, 16))
                letters[letter][pos] = character

    with open(output_file, "w") as file:
        file.write(u"var hiraganaToKatakanaMap = {\n")
        for letter, characters in letters.iteritems():
            if not all(characters):
                missing = "hiragana" if not characters[pos_hiragana] else "katakana"
                print "warning: no {} equivalent for '{}'".format(missing, letter)
                continue
            hiragana = characters[pos_hiragana]
            katakana = characters[pos_katakana]
            file.write(u'  "{}": "{}",\n'.format(hiragana, katakana).encode("utf-8"))
        file.write(u"};\n")

if __name__ == '__main__':
    main(*sys.argv[1:])
