def backtrack(digits, path, result, phone_map,count):
    # Base case: if the current path has the same length as the digits string, add the path to result
    if len(path) == len(digits):
        result.append("".join(path))
        return
    # For the current digit, iterate over all its corresponding letters
    
    for letter in phone_map[digits[len(path)]]:
        # Choose: Add the letter to the path
        print(count,path, len(path))
        path.append(letter)
        # Explore: Recursively permute the rest
        backtrack(digits, path, result, phone_map,count+1)
        # Un-choose (Backtrack): Remove the last added letter
        path.pop()


def letterCombinations(digits):
    if not digits:
        return []

    # Mapping of digits to their corresponding letters
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

    result = []
    backtrack(digits, [], result, phone_map, 0)
    return result


# Example usage
print(letterCombinations("234"))
