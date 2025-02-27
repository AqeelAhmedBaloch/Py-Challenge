# Day-4 Challenge
from num2words import num2words

def number_to_word(n):
    return num2words(n)

print("In words:", number_to_word(int(input("Enter a number: "))))