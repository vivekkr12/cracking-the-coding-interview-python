def is_one_away(a: str, b: str) -> bool:
    len_a, len_b = len(a), len(b)

    if abs(len_a - len_a) > 1:
        return False

    pa, pb = 0, 0
    count_diffs = 0
    while pa < len_a and pb < len_b:
        if a[pa] == b[pb]:
            pa += 1
            pb += 1
        else:
            count_diffs += 1
            if len_a > len_b:
                pa += 1
            elif len_b > len_a:
                pb += 1
            else:
                pa += 1
                pb += 1

    if len_a - pa > 0 or len_b - pb > 0:
        count_diffs += 1

    return count_diffs == 1


if __name__ == '__main__':
    tests = [("a", "b", True),
             ("", "d", True),
             ("d", "de", True),
             ("pale", "pse", False),
             ("acdsfdsfadsf", "acdsgdsfadsf", True),
             ("acdsfdsfadsf", "acdsfdfadsf", True),
             ("acdsfdsfadsf", "acdsfdsfads", True),
             ("acdsfdsfadsf", "cdsfdsfadsf", True),
             ("adfdsfadsf", "acdfdsfdsf", False),
             ("adfdsfadsf", "bdfdsfadsg", False),
             ("adfdsfadsf", "affdsfads", False),
             ("pale", "pkle", True),
             ("pkle", "pable", False)]

    for ta, tb, t_actual in tests:
        t_res = is_one_away(ta, tb)
        print('a: {}, b: {}, actual: {}, result: {}, match: {}'.format(ta, tb, t_actual, t_res, t_actual == t_res))
        if t_actual != t_res:
            raise Exception('Test case failed')
