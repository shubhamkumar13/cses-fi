class Solution:
    def __init__(self, size : int, nums : [int]):
        self.size = size
        self.nums = nums
    
    def solve(self) -> int:
        total_nums = set(i for i in range(1, self.size + 1))
        nums = set(self.nums)
        return total_nums.difference(nums).pop()

def main():
    length = int(input())
    numbers = list(map(int, input().split(" ")))
    o = Solution(length, numbers)
    print(o.solve())

if __name__ == "__main__":
    main()