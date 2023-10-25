# op1 : 1 from LEFT and 2 from RIGHT
# op2 : 2 from LEFT and 1 from RIGHT
from sys import stdin, stdout

def main():
    t = int(stdin.readline())
    for _ in range(t):
        [a, b] = map(int, stdin.readline().split(" "))
        # a = x + 2y
        # b = y + 2x
        # x = 2b - a / 3 > 0 : condition 1
        # y = 2a - b / 3 > 0 : condition 2
        # (a + b) / 3 = x + y is a whole number : condition 3 
        # so if (a + b) % 3 == whole number then YES else NO
        # easy to check any one is false
        if (a + b) % 3 != 0 or (a - 2*b > 0) or (b - 2*a > 0) :
            stdout.write("NO" + "\n")
        else:
            stdout.write("YES" + "\n")

if __name__ == "__main__":
    main()