class Solution:
    def __init__(self, input: str):
        self.input = input
        self.size = len(input)
    
    def largest(self) -> int:
        lst = []
        t = 1

        for i in range(0, self.size - 1):
            if self.input[i] == self.input[i + 1]:
                t = t + 1
            else:
                lst.append(t)
                t = 1
        
        lst.sort()
        return lst.pop()

from sys import stdin

def main():
    sequence = stdin.readline()
    o = Solution(sequence)
    print(o.largest())

if __name__ == "__main__":
    main()