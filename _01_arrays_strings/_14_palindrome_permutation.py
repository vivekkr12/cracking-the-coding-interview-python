def is_palindrome_permutation(s: str) -> bool:
    freq_dict = dict()
    len_ = 0
    for char in s:
        if not char.isalpha():
            continue

        char = char.lower()
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1

        len_ += 1

    odd_allowed = len_ % 2 == 1
    for _, freq in freq_dict.items():
        if freq % 2 == 1:
            if odd_allowed:
                odd_allowed = False
                continue
            else:
                return False

    return True


if __name__ == '__main__':
    strings = ["Rats live on no evil star",
               "A man, a plan, a canal, panama",
               "Lleve",
               "Tacotac",
               "asda"]

    for x in strings:
        res = is_palindrome_permutation(x)
        print(x)
        print(res)
        print('---')
