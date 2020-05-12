def is_permutation(s1: str, s2: str) -> bool:
    # assume fixed char set
    char_set = [0] * 128
    for x in s1:
        index = ord(x)
        char_set[index] += 1

    for x in s2:
        index = ord(x)
        char_set[index] -= 1

    for count in char_set:
        # check must be of !=0 as the count can be less than or equal to 0
        if count != 0:
            return False

    return True


if __name__ == '__main__':
    pairs = [("apple", "papel"), ("carrot", "tarroc"), ("hello", "llloh")]
    for str1, str2 in pairs:
        print('{} | {}: {}'.format(str1, str2, is_permutation(str1, str2)))
