def validPalindrome( s):
    def is_palindrome(left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left, right = 0, len(s) - 1

    # Check for palindrome
    while left < right:
        if s[left] != s[right]:
            # Try skipping the character at left or at right
            return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
        left += 1
        right -= 1

    return True  # If no mismatches were found, it's already a palindrome

temp={'a':'dasdas'}
print(temp.get('b',0)
print(temp)