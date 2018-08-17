# functions

# Example - Adding two numbers and print it

import argparse
import sys

def sum_of_two_numbers(a,b):
    """This functiono finds sum of two numbers"""
    print(a+b)


parser = argparse.ArgumentParser(description = "Adds two numbers")
parser.add_argument("num1", type=int, help="1st number")
parser.add_argument("num2", type=int, help="2nd number")

args = parser.parse_args()

# call the function.
sum_of_two_numbers(int(args.num1), int(args.num2))

