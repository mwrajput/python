x = 121

if x < 0:
    print(False)  # Negative numbers are not palindromes
else:
    # Reverse the integer
    original = x
    reversed_num = 0

    while x > 0:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10

    # Check if the reversed integer is the same as the original
    print("Is it Palindrome : ",original == reversed_num)
