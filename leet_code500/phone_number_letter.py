def letterCombinations(digits):
    if not digits:
        return []

    # Mapping of digits to corresponding letters
    phone_map = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def backtrack(index, current_combination, result):
        # Base case: If the combination length matches the digits length, add to result
        if index == len(digits):
            result.append("".join(current_combination))
            return

        # Get possible letters for the current digit
        current_digit = digits[index]
        for letter in phone_map[current_digit]:
            current_combination.append(letter)  # Choose
            backtrack(index + 1, current_combination, result)  # Explore
            current_combination.pop()  # Un-choose (Backtrack)

    result = []
    backtrack(0, [], result)
    return result

# Example Usage
print(letterCombinations("23"))
# Output: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
