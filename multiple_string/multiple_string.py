num1 = "123"
num2 = "456"

# Convert the strings to arrays of integers
nums1 = [int(ele) for ele in num1]
nums2 = [int(ele) for ele in num2]

n1 = len(nums1)
n2 = len(nums2)

# Initialize the product array with zeros
product = [0] * (n1 + n2)

# Perform the multiplication
for i in range(n1 - 1, -1, -1):
    carry = 0
    for j in range(n2 - 1, -1, -1):
        # Multiply the digits
        pr = nums1[i] * nums2[j]
        # Add to the current position (including carry)
        temp_sum = product[i + j + 1] + pr + carry
        product[i + j + 1] = temp_sum % 10  # Update the current digit
        carry = temp_sum // 10  # Update the carry
    # Add any remaining carry to the next position

    product[i + j] += carry

# Remove leading zeros from the product array
while len(product) > 1 and product[0] == 0:
    product.pop(0)

# Convert the product array to a string
result = ''.join(map(str, product))
print(result)
res=[]
if res:
    print('sadsad')