def multiple(str1, str2):
    result = [0] * (len(str1) + len(str2))  # Correct size of result array
    str1=str1[::-1]
    str2=str2[::-1]
    for i in range(len(str1)):  # Reverse loop for correct multiplication order
        k = i  # Adjusted k for correct index handling
        carry = 0
        for j in range(len(str2)):  # Reverse loop for correct order
            prod = int(str1[i]) * int(str2[j]) + carry + result[k]
            carry = prod // 10
            result[k] = prod % 10
            k += 1

        result[k] += carry  # Carry should be added at the next index

    # Convert result list to string and remove leading zeros
    while len(result) > 1 and result[-1] == 0:
        result.pop()

    return "".join(map(str, result[::-1]))  # Reverse the result to get the final product


# Test case
print(multiple('3', '2'))  # Output: "1728"
