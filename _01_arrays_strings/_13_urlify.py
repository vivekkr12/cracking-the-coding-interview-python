from typing import List


def replace_spaces(s: List):
    n = len(s)
    last_char_pos = -1
    for i in reversed(range(0, n)):
        if s[i] != ' ':
            last_char_pos = i
            break

    src, target = last_char_pos, n - 1

    while src >= 0:
        if s[src] != ' ':
            s[target] = s[src]
            src -= 1
            target -= 1
        else:
            s[target] = '0'
            s[target - 1] = '2'
            s[target - 2] = '%'

            src -= 1
            target -= 3

        if target <= src:
            break


if __name__ == '__main__':
    input_str_tuple = (list("Mr John Smith    "), list("EndOfWorld"))
    for input_str in input_str_tuple:
        print('Before: {}'.format(''.join(input_str)))
        replace_spaces(input_str)
        print('After: {}'.format(''.join(input_str)))
        print('---')
