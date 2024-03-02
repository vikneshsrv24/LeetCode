# Time complexity:
# O(nlogn) due to sort() function.
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums=[i**2 for i in nums]
        nums.sort()
        return nums


# Two pointer method
# O(n) -> Time complexity
  class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        start, end = 0, n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[start]) >= abs(nums[end]):
                ans[i] = nums[start] * nums[start]
                start += 1
            else:
                ans[i] = nums[end] * nums[end]
                end -= 1
        return ans

