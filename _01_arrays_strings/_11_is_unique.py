# straight forward solution: use a set
def is_unique(s: str) -> bool:
    chars = set()
    for x in s:
        if x in chars:
            return False
        chars.add(x)
    return True


# Use an array assuming fixed char set
def is_unique_arr(s: str) -> bool:
    char_set = [False] * 128
    for x in s:
        index = ord(x)
        if char_set[index]:
            return False
        char_set[index] = True

    return True


# If no other data structure has to be used:
# 1. compare each char with every other char - O(N^2)
# 2. sort the array and then compare - O(Nlog(N))
if __name__ == '__main__':
    words = ["abcde", "hello", "apple", "kite", "padle"]
    for word in words:
        print('{}: {} | {}'.format(word, is_unique(word), is_unique_arr(word)))
