class Solution:
    def subsets(self, nums):
        return self.subsetsRecur([], sorted(nums))

    def subsetsRecur(self, current, nums):
        if nums:
            return self.subsetsRecur(current, nums[1:]) + self.subsetsRecur(current + [nums[0]], nums[1:])
        return [current]


print(Solution().subsets([4, 5, 6]))
