from sys import stdin, stdout, maxsize
from copy import copy

INFINITY = maxsize

def calculate_set(sum_n : int, lst : [int]) -> [int]:
    output_lst = []
    lst.reverse()
    for i in lst:
        if i <= sum_n:
            sum_n = sum_n - i
            output_lst.append(i)
    
    return output_lst
        

def main():
    n = int(stdin.readline())
    lst = list(range(1, n + 1))

    sum_n = n * (n + 1) // 2

    if sum_n % 2 != 0:
        print("NO")
    
    first_lst = calculate_set(sum_n // 2, copy(lst))
    first_set = set(first_lst)
    lst = set(lst)
    second_lst = list(lst.difference(first_set))

    first_len = len(first_lst)
    second_len = len(second_lst)
    first = " ".join(map(str, first_lst))
    second = " ".join(map(str, second_lst))

    stdout.write("YES" 
                 + "\n" 
                 + str(first_len) 
                 + "\n" 
                 + str(first) 
                 + "\n" 
                 + str(second_len) 
                 + "\n"
                 + str(second)
                 + "\n")

if __name__ == "__main__":
    main()