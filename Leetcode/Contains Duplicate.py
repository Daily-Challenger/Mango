def containsDuplicate(nums: list[int]) -> bool:
    checked = []
    for i in range(len(nums)):
        checked.append(nums[i])
        if i < len(nums) - 1 and nums[i + 1] in checked:
            return True
    return False


def containsDuplicate_optimized(self, nums: list[int]) -> bool:
    checked = set()
    for num in nums:
        if num in checked:
            return True
        checked.add(num)
    return False


print(containsDuplicate([1,2,3,1]))