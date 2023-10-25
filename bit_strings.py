from sys import stdin, stdout
from math import pow, ceil

def main():
    i = int(stdin.readline())
    res = 1
    mod = ceil(pow(10, 9) + 7)
    for _ in range(i):
        res = res * 2
        res = res % mod
    
    stdout.write(str(res))

if __name__ == "__main__":
    main()