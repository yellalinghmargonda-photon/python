def LCSLength(X, Y,m,n):
    # return if the end of either sequence is reached
    if m == 0 or n == 0:
        return 0
        # if the last character of `X` and `Y` matches
    if X[m - 1] == Y[n - 1]:
        return LCSLength(X, Y, m - 1, n - 1) + 1
    # otherwise, if the last character of `X` and `Y` don't match
    return max(LCSLength(X, Y, m, n - 1), LCSLength(X, Y, m - 1, n))


X = 'ABCBDAB'
Y = 'BDCABA'

print('The length of the LCS is', LCSLength(X, Y, len(X), len(Y)))

def LCSLength(X, Y,m,n,lookup):
    # return if the end of either sequence is reached
    if m == 0 or n == 0:
        return 0
    key = (m, n)
    # if the subproblem is seen for the first time, solve it and
    # store its result in a dictionary
    if key not in lookup:

        # if the last character of `X` and `Y` matches
        if X[m - 1] == Y[n - 1]:
            lookup[key] = LCSLength(X, Y, m - 1, n - 1, lookup) + 1

        else:
            # otherwise, if the last character of `X` and `Y` don't match
            lookup[key] = max(LCSLength(X, Y, m, n - 1, lookup),
                              LCSLength(X, Y, m - 1, n, lookup))

    # return the subproblem solution from the dictionary
    return lookup[key]

X = 'ABCBDAB'
Y = 'BDCABA'

# create a dictionary to store solutions to subproblems
lookup = {}

print('The length of the LCS is', LCSLength(X, Y, len(X), len(Y), lookup))

def LCSLength(X, Y):
    m, n = len(X), len(Y)

    # Step 1: Create a DP table initialized to 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Step 2: Fill the table bottom-up
    for i in range(1, m + 1):  # Iterate over X
        for j in range(1, n + 1):  # Iterate over Y
            if X[i - 1] == Y[j - 1]:  # Matching characters
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:  # Take max of two cases
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Step 3: Return the final LCS length
    return dp[m][n]

# Example Usage
X = 'ABCBDAB'
Y = 'BDCABA'

print('The length of the LCS is', LCSLength(X, Y))

