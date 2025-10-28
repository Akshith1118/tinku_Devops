def is_palindrome(s):
    # Clean input: ignore non-alphanumeric and case
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        input_str = sys.argv[1]
        if is_palindrome(input_str):
            print("Palindrome")
            exit(0)
        else:
            print("Not a palindrome")
            exit(1)
    else:
        print("Usage: python palindrome_checker.py <string>")
        exit(2)
