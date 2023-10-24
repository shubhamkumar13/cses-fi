from sys import stdin, stdout, maxsize

INFINITY = maxsize
MEM = {}

def solve(x : int, i : [int]) -> int:

    contains = MEM.get(x)
    if contains:
        return contains

    if x == 0:
        return 0
    
    if x < 0:
        return INFINITY
    
    res_x = min(map(lambda c : solve(x - c, i) + 1, i))
    MEM.update({x : res_x})
    return res_x

def main():
    i = [1, 3, 4]
    x = 1000
    out = solve(x, i)
    print(out)

if __name__ == "__main__":
    main()