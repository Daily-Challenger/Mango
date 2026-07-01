def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        pairnum = target - nums[i]
        if pairnum in nums and nums.index(pairnum) != i:
            return [nums.index(pairnum),i]

print(twoSum([3,3], 6))