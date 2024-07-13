def sortColors(self, nums):
    zero = -1
    one = -1
    two = -1

    for num in nums:
        if num == 0:
            two += 1
            nums[two] = 2
            one += 1
            nums[one] = 1
            zero += 1
            nums[zero] = 0
        elif num == 1:
            two += 1
            nums[two] = 2
            one += 1
            nums[one] = 1
        else:
            two += 1
            nums[two] = 2
            
            
print(sortColors([2,0,2,1,1,0]))
