class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        actual_sum=n*(n+1)//2
        sum=0

        for num in nums:
            sum+=num
        return actual_sum-sum
        