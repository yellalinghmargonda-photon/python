def generateParenthesis(n):
    result = []

    def backtrack(current, open_count, close_count):
        # Base case: if the current string is of length 2*n (we've used all parentheses)
        if len(current) == 2 * n:
            result.append(current)
            return

        # Add an opening parenthesis if we haven't used n opening parentheses
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)

        # Add a closing parenthesis if the number of closing parentheses is less than the opening ones
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)

    # Start backtracking with an empty string and 0 open and close counts
    backtrack("", 0, 0)

    return result


# Example usage:
n = 3
print(generateParenthesis(n))
