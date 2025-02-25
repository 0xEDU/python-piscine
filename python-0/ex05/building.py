import sys


def main():
    try:
        assert len(sys.argv) <= 2, "more than one argument provided"

        inputTxt = ''
        if len(sys.argv) == 1:
            inputTxt = input('What is the text to count?\n')
        else:
            inputTxt = sys.argv[1]
        special = r'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
        uppers = sum(1 for c in inputTxt if c.isupper())
        lowers = sum(1 for c in inputTxt if c.islower())
        puncts = sum(1 for c in inputTxt if c in special)
        spaces = sum(1 for c in inputTxt if c.isspace())
        digits = sum(1 for c in inputTxt if c.isdigit())
        print(f'{uppers} uppercase letters\n' +
              f'{lowers} lowercase letters\n' +
              f'{puncts} punctuation characters\n' +
              f'{spaces} spaces\n' +
              f'{digits} digits')

    except AssertionError as e:
        print(f'{e.__class__.__name__}: {e}')
        sys.exit(1)


if __name__ == "__main__":
    main()
