def LIS(arr,i, n, prev):
    if i == n:
        return 0
    # case 1: exclude the current element and process the
    # remaining elements
    excl = LIS(arr, i + 1, n, prev)
    # case 2: include the current element if it is greater
    # than the previous element in LIS
    incl = 0
    if arr[i] > prev:
        incl = 1 + LIS(arr, i + 1, n, arr[i])

    # return the maximum of the above two choices
    return max(incl, excl)


arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

print('The length of the LIS is', LIS(arr, 0, len(arr), float('-inf')))


def lengthOfLIS( nums) -> int:
    # Initialize LIS array with 1, as the minimum length of LIS for any element is 1
    dp = [1] * len(nums)
    for j in range(1, len(nums)):
        for i in range(j):
            if nums[j] > nums[i]:
                dp[j] = max(dp[j], 1 + dp[i])
    return max(dp)


def LIS2(nums):
    n = len(nums)

    # Create the DP table with dimensions (n + 1) x (n + 1)
    # dp[i][j] represents the length of LIS starting at index i with the last included element at j
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Fill the DP table from bottom up
    for i in range(n - 1, -1, -1):  # Start from the last element and move to the first
        for prev_index in range(i, -1, -1):  # Consider all previous indices
            # Option 1: Exclude the current element (move to the next index)
            excl = dp[i + 1][prev_index]

            # Option 2: Include the current element (if it is greater than the element at prev_index)
            incl = 0
            if prev_index == -1 or nums[i] > nums[prev_index]:
                incl = 1 + dp[i + 1][i]

            # Store the maximum of including or excluding the current element
            dp[i][prev_index] = max(incl, excl)

    # The answer is in dp[0][-1], which is the length of the LIS starting at index 0 with no previous element
    return dp[0][-1]

def LIS(index, prev_index, nums):
    if index==len(nums):
        return 0
    exlucde= LIS(index+1, prev_index,nums)
    include=0
    if prev_index==-1 or nums[index]>nums[prev_index]:
        include=1+LIS(index+1, index,nums)
    return max(include,exlucde)