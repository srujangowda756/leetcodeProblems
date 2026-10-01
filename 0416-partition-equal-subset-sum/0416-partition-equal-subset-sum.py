class Solution:
    def help(self, nums, target, i, dp):
        if target == 0:
            return True

        if i == len(nums) or target < 0:
            return False

        if (i, target) in dp:
            return dp[(i, target)]

        take = self.help(nums, target - nums[i], i + 1, dp)
        skip = self.help(nums, target, i + 1, dp)

        dp[(i, target)] = take or skip

        return dp[(i, target)]

    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        dp = {}

        return self.help(nums, target, 0, dp)