import sys


def find(n, k):
    if n >= k:
        return n - k
    if n == 0:
        return 1 + find(n + 1, k)
    if k % 2 == 0:
        return min(k - n, find(n, k // 2))
    return 1 + min(find(n, k + 1), find(n, k - 1))


if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    print(find(n, k))

# TC
# 5 17

# 2