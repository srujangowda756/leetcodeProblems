class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        ans = nums[0]
        max_cur = nums[0]
        min_cur = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_cur, min_cur = min_cur, max_cur

            max_cur = max(nums[i], max_cur * nums[i])
            min_cur = min(nums[i], min_cur * nums[i])

            ans = max(ans, max_cur)

        return ans