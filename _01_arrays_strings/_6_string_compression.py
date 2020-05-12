def compress_string(string: str) -> str:
    n_original = len(string)
    if n_original <= 1:
        return string

    compressed_str = []

    curr_char = string[0]
    i = 1
    count_curr_char = 1
    while i < n_original:
        if string[i] == curr_char:
            count_curr_char += 1
        else:
            compressed_str.append(curr_char)
            compressed_str.append(str(count_curr_char))
            curr_char = string[i]
            count_curr_char = 1

        i += 1

    if count_curr_char >= 1:
        compressed_str.append(curr_char)
        compressed_str.append(str(count_curr_char))

    n_compressed = len(compressed_str)

    return ''.join(compressed_str) if n_compressed < n_original else string


if __name__ == '__main__':
    tests = [
        "aaaaabbbbaaaabbddc",
        "aabcccccaaa",
        "abcd",
        "",
        "a"
    ]

    for t in tests:
        print('{}: {}'.format(t, compress_string(t)))
