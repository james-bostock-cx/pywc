import sys

def wc(filename):

    lines = 0
    words = 0
    chars = 0

    with open(filename) as f:
        for line in f.readlines():
            lines = lines + 1
            words = words + len(line.split())
            chars = chars + len(line) + 1

    print(f'{filename}: {lines} {words} {chars}')

    return (lines, words, chars)


if __name__ == '__main__':

    count = 0
    lines = 0
    words = 0
    chars = 0

    for arg in sys.argv[1:]:
        count = count + 1
        (l, w, c) = wc(arg)
        lines = lines + l
        words = words + w
        chars = chars + c

    if count > 1:
        print(f'Total: {lines} {words} {chars}')
