#Day-6 Challenge

try:
    print("Palindrome Mini Project\n")
    num_int = int(input("Enter Integer Number : "))
    binary_num = bin(num_int)[2:]

    print(f"Binary Representation: {binary_num}")
    print("Palindrome ✅" if binary_num == binary_num[::-1] else "Not a Palindrome ❎")
except ValueError:
    print("Invalid Input! Please Enter Integer Number ❌.")