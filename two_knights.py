from sys import stdin, stdout

def peaceful_positions(n : int):
    def total_positions(n : int):
        # nC2 on n x n board
        # n x n == total positions on board
        # K1 <- n^2, K2 <- n^2 - 1
        # and replacing K1 with K2 
        # and K2 with K1 gives the same arrangement
        # so divide by 2

        return ((n * n) * ((n * n) - 1)) // 2
    
    def attack_positions(n : int):
        # every 2 x 3 box has 4 unique positions
        # where 2 knights are at attacking positions
        # similarly for a 3 x 2 box
        # and every 3 x 2 box occupies n - 1 places horizontally 
        # and n - 2 vertically.
        # and every 2 x 3 box occupies n - 1 places vertically
        # and n - 2 horizontally

        return (2 * 2 * (n - 1) * (n - 2))

    for i in range(1, n + 1):
        res = total_positions(i) - attack_positions(i)
        stdout.write(str(res) + "\n")

def main():
    n = int(stdin.readline())
    peaceful_positions(n)

if __name__ == "__main__":
    main()