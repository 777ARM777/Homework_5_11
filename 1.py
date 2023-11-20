class Solution:
    def twoSum(self, lst: List[int], target: int) -> List[int]:
        numbers = sorted(lst)
        left = 0
        right = len(numbers) - 1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [lst.index(numbers[left]), len(lst) - lst[::-1].index(numbers[right]) - 1]
            elif s > target:
                right -= 1
            else:
                left += 1
        return [-1, -1]


