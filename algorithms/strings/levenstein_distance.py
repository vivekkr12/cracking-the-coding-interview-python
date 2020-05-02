# transform string X to string Y using only three operations
# 1. insert (cost 1)
# 2. deletion (cost 1)
# 3. substitution (cost 2)


def min_levenstein_distance(x: str, y: str) -> int:
    len_x, len_y = len(x), len(y)
    distances_last = list(range(len_y + 1))
    for i in range(1, len_x + 1):
        # distance of '' (blank) to i
        dist1 = i
        distances_curr = [0] * (len_y + 1)
        for j in range(1, len_y + 1):
            # distance of j - 1 -> i
            dist1 = dist1 + 1

            # distance of i - 1 -> j
            dist2 = distances_last[j] + 1

            # distance of i - 1 > j - 1
            dist3 = distances_last[j - 1] if x[i - 1] == y[j - 1] else distances_last[j - 1] + 2

            min_dist = min(dist1, dist2, dist3)
            distances_curr[j] = min_dist
            dist1 = min_dist

        distances_curr[0] = i
        distances_last = distances_curr

    return distances_last[-1]


if __name__ == '__main__':
    tests = [
        ('execution', 'intention'),
        ('python', 'python'),
        ('abc', 'dbe'),
        ('asshole', 'cunt'),
    ]

    for tx, ty in tests:
        print('{}, {} : {}'.format(tx, ty, min_levenstein_distance(tx, ty)))
