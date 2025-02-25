import sys

try:
    if len(sys.argv) == 1:
        sys.exit(0)
    assert len(sys.argv) == 2, "more than one argument is argument is provided"
    num = sys.argv[1].replace('-', '', 1)
    if not num.isdigit():
        raise AssertionError("argument is not an integer")
    num = int(num)
    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

except AssertionError as e:
    print(f'{e.__class__.__name__}: {e}')
    sys.exit(1)
