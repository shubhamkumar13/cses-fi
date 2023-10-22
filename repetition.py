class Solution:
    def __init__(self, input: str):
        self.input = input
    
    def largest(self) -> int:
        lst = []
        temp = self.input[0]
        rest = self.input[1:]

        for s in rest:
            if temp[0] == s:
                temp = temp + s
            else:
                lst.append(temp)
                temp = s
        
        lst = list(map(len, lst))
        return lst.pop()

def main():
    sequence = input().strip()
    sequence = [ch for ch in sequence]
    o = Solution(sequence)
    print(o.largest())

if __name__ == "__main__":
    main()