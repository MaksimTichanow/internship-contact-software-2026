# Eigenes Package
import sys
import os



# Funktionen

def iterate_word(word):
    for i in word:
        print(i)

def fib(n):
    """Write Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fib2(n):
    """Return Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

def print_filename():
    sys.argv[0]


def sum_list(your_list):
    summe = 0
    for num in your_list:
        summe = summe + num
        print(summe)
    print(f"Die Summe deiner List ist: {summe}")

def string_length(word):
    print(len(word))


def biggest_float():
    print(sys.float_info.max)

