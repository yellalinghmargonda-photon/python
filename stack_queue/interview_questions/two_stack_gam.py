#gothorught the notes to get the key points
def twostackgam(max_sum,stack1,stack2,runnig_Sum,count):
    if max_sum<runnig_Sum:
        return count-1
    if (len(stack1)==0 or len(stack2)==0 ):
        return count-1

    count1= twostackgam(max_sum, stack1[1::], stack2, runnig_Sum=runnig_Sum + stack1[0], count=count+1)
    count2 = twostackgam(max_sum, stack1, stack2[1::], runnig_Sum=runnig_Sum + stack2[0], count=count + 1)
#take max because each recursion  will give its own answer we have to pick the one with max
    return max(count1,count2)
stack1=[4,2,4,6,1]
stack2=[2,1,8,5]

max_count=twostackgam(10, stack1=stack1,stack2=stack2,runnig_Sum=0,count=0)
print(max_count)

