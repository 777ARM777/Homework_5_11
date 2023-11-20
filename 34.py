class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        index = -1
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                index = mid
                break
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        if index == -1:
            return [-1, -1]
        e = s = index
        while s >= start and nums[s] == target:
            s -= 1
        while e <= end and nums[e] == target:
            e += 1
        return [s + 1, e - 1]