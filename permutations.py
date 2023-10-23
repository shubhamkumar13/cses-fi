from sys import stdin, stdout

class Solution:
    def permute(self, n):

        if n == 2 or n == 3 :
            stdout.write("NO SOLUTION")
            return
        
        # print all the even values
        for i in range(2, n+1, 2):
            stdout.write(str(i) + " ")
        
        # print all the odd values
        for i in range(1, n+1, 2):
            stdout.write(str(i) + " ")
        
        return

def main():
    i = int(stdin.readline())
    o = Solution()
    o.permute(i)

if __name__ == "__main__":
    main()