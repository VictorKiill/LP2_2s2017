def maior_ponta(nums):
    nums2 = []  
    if len(nums) > 0 and nums[0] >= nums[len(nums)-1]:
        while len(nums2) < len(nums):
            nums2.append(nums[0])
    elif len(nums) > 0:
        while len(nums2) < len(nums):
            nums2.append(nums[len(nums)-1])
    return nums2