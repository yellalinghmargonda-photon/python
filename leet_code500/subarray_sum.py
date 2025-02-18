def subarraySum(nums,k) -> int:
        count = 0
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[i - 1] + nums[i])
        # we haveto check sum(j,i)=prefix[i]-prefix[j-1]=k
        # prefix[j-1]=prefix[i]-k
        # this is nothing but for any index has there been a sub array preor to i whose sum is prefix[i]-k
        hashmap = {0: 1}
        for i in  range(len(nums)):
            if prefix_sum[i] - k in hashmap:
                count += hashmap[prefix_sum[i] - k]
            if prefix_sum[i] in hashmap:
                hashmap[prefix_sum[i]] = hashmap[prefix_sum[i]] + 1
            else:
                hashmap[prefix_sum[i]] = 1
        return count

nums = [1,1,1]
k = 2
print(subarraySum(nums,k))