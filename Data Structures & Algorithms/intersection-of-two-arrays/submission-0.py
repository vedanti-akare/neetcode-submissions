class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1=set(nums1)
        result=[]

        for num in set1:
            if num in nums2:
                result.append(num)
        return result