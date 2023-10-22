from sys import stdin

class Solution:

    def __init__(self, input):
        self.input = input
    
    def num_moves(self) -> int:
        input = self.input
        temp = input[0]
        rest = input[1:]
        moves = 0

        for i in rest:
            if temp <= i:
                temp = i
                continue
            moves += temp - i
        
        return moves


def main():
    _ = stdin.readline()
    input = stdin.readline()
    input = list(map(int, input.strip().split(" ")))
    o = Solution(input)
    print(o.num_moves())

if __name__ == "__main__":
    main()