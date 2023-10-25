from sys import stdin, stdout
from math import ceil

def calculate_multiple_of_5(n : int) -> int:
    counter = 0
    k = 5
    p = 5
    while (n // p) != 0:
        counter = counter + (n // p)
        p = p * k
    
    return counter

def main():
    n = int(stdin.readline())
    zeros = calculate_multiple_of_5(n)
    stdout.write(str(zeros) + "\n")

if __name__ == "__main__":
    main()