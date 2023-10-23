from sys import stdout, stdin

def last_spiral_value(y : int, x : int) -> int:
#      1       2        3       4
#    1 00, 1  | 01, 2  | 02, 9  | 03, 10
#    2 10, 4  | 11, 3  | 12, 8  | 13, 11
#    3 20, 5  | 21, 6  | 22, 7  | 23, 12
#    4 30, 16 | 31, 15 | 32, 14 | 33, 13

    # Logic :
        
    # if I need to figure out value of an element 
    # in the spiral I need 2 things
    
    # 1. max of row and column, why? : 
    #     1.1 because the spiral works on a square matrix
    #     1.2 getting the max helps in figuring out the max value on the border
    #     1.3 Why border? Because it doesn't matter what your value is, it is 
    #         always placed on the border a value at index (1, 4) will be on the
    #         border of 4x4 square matrix. 
    # 2. How do we move from finding the max border value
    #     2.1 Getting the max value now helps in moving up or down the border
    #     2.2 If the max value is even
    #         vertically increases
    #         horizontally decreases
    #     2.3 If the max value is odd
    #         vertically decreases
    #         horizontally increases
    # 3. max^2 is the largest value in the border
    #    If even :
    #     decrease the value by (max - 1) + (vertical - horizontal)
    #    If odd :
    #     decrease the value by (max - 1) + (horizontal - decreases)
    #
    # so in the above since we are by default decreasing from the max value we
    # need to know how much was increased by
    # WHAT-INCREASES - WHAT-DECREASES
        # IF Decreases is more then
    # MAX - 1 to move to corner (even)
    # also imagine this on a long strip : 
    # 16, 15, 14, 13, 12, 11, 10
    # 16 - (4 - 1) - (horizontal - vertical)
    # so 2 (vertical), 4 (horizontal) : 16 - 3 + (-2) => 11 
       

    # y <- vertical, x <- horizontal
    # m = max(x,y)
    # if m is even then x, y = y, x
    # print(m^2 - (m + y - (x + 1)))

    lst = [[]]
    m = max(x,y)
    m_sq = m * m
    # 4, 2
    if m % 2 == 0:
        # change horizontal to vertical and vertical to horizontal
        x, y = y, x
        return m_sq - (m - 1) + (x - y)
    else:
    # 3, 2
        return m_sq - (m - 1) + (x - y)

def main():
    t = int(stdin.readline())
    lst = []

    for _ in range(t):
        [y, x] = stdin.readline().strip().split(" ")
        lst.append(last_spiral_value(int(y), int(x)))
    
    for i in lst:
        print(i)
    
if __name__ == "__main__":
    main()