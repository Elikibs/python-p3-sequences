#!/usr/bin/env python3

def print_fibonacci(length):
    # Initialize the fisrt two fibonacci numbers
    a, b = 0, 1

    while a < length:
        # Print the current fibonnaci number and add space without moving to the next line using (end = "")
        print(a, end=" ")
        # It updates the variables a and b to the next pair of Fibonacci numbers. 
        # The new value of a becomes the old value of b, and the new value of b becomes the sum of the old values of a and b.
        a, b = b, a+b
    print()

print(print_fibonacci(9))