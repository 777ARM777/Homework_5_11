class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 1
        while i >= 1 and nums[i] <= nums[i - 1]:
            i -= 1
        if i > 0:
            j = i
            while j < len(nums) and nums[j] > nums[i - 1]:
                j += 1
            nums[j - 1], nums[i - 1] = nums[i - 1], nums[j - 1]
        nums[i:] = reversed(nums[i:])