nums=[2, 3, 1, 4]
n=len(nums)
left=[1]*n
right=[1]*n
prod=[1]*n
for i in range(1,len(nums)):
    left[i]=left[i-1]*nums[i-1]
j=len(nums)-2
while j>=0:
    right[j]=right[j+1]*nums[j+1]
    j-=1
for i in range(len(nums)):
    prod[i]=left[i]*right[i]
