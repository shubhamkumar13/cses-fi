class Solution:

    def __init__(self):
        self.mem = {}
    
    def __repr__(self):
        return str(self.mem)
    
    def has(self, n : int) -> int:
        self.mem.get(n)

    def to_list(self) -> [int]:
        t = []

        for k, _ in self.mem.items():
            t.append(k)
        return t
    
    def formula(self, n:int) -> int:
        if (n % 2) == 0:
            return n // 2
        else:
            return (3 * n + 1)
    
    def calculate(self, n : int) -> [int]:
        if n == 1:
            return [1]

        current = self.has(n)

        if current:
            return self.calculate(current)
        
        f = self.formula(n)
        self.mem.update({n : f})
        
        if f == 1:
            l = self.to_list()
            l.append(f)
            return l
        else:
            return self.calculate(f)

def main():
    i = int(input())
    o = Solution()
    output = map(str, o.calculate(i))
    print(' '.join(output))

if __name__ == "__main__":
    main()