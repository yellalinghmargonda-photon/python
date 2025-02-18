from itertools import permutations

# Global dictionary to store letter-to-digit mappings
letter_to_digit = {}


def puzzle_solved(puzzle):
    """Check if the current digit assignment satisfies the equation."""
    addend1, addend2, result = puzzle
    num1 = word_to_number(addend1)
    num2 = word_to_number(addend2)
    num_result = word_to_number(result)

    return (num1 + num2) == num_result


def word_to_number(word):
    """Convert a word to a number using the current letter-to-digit mapping."""
    return int("".join(str(letter_to_digit[c]) for c in word))


def assign_letter_to_digit(letter, digit):
    """Assign a digit to a letter if not already used."""
    if digit in letter_to_digit.values():  # Ensure unique assignment
        return False
    letter_to_digit[letter] = digit
    return True


def unassign_letter_from_digit(letter, digit):
    """Remove the assigned digit from the letter mapping (backtracking step)."""
    if letter in letter_to_digit:
        del letter_to_digit[letter]


def exhaustive_solve(puzzle, letters_to_assign):
    """Recursively attempt to solve the cryptarithmetic puzzle."""
    if not letters_to_assign:  # No more letters to assign
        return puzzle_solved(puzzle)

    letter = letters_to_assign[0]  # Pick the first unassigned letter
    for digit in range(10):  # Try all digits (0-9)
        if assign_letter_to_digit(letter, digit):  # If assignment is valid
            if exhaustive_solve(puzzle, letters_to_assign[1:]):  # Recurse
                return True
            unassign_letter_from_digit(letter, digit)  # Backtrack

    return False  # No valid solution found, backtrack further


def solve_cryptarithmetic(puzzle):
    """Wrapper function to extract unique letters and start the solving process."""
    unique_letters = sorted(set("".join(puzzle)))

    if len(unique_letters) > 10:
        return "Too many unique letters to solve with digits (0-9)"

    global letter_to_digit
    letter_to_digit = {}  # Reset global mapping

    if exhaustive_solve(puzzle, unique_letters):
        return letter_to_digit
    return "No solution found"


# Example usage
puzzle = ("SEND", "MORE", "MONEY")  # SEND + MORE = MONEY
solution = solve_cryptarithmetic(puzzle)

if isinstance(solution, dict):
    print("Solution Found:")
    for letter, digit in solution.items():
        print(f"{letter} = {digit}")
else:
    print(solution)
