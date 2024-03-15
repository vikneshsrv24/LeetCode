class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:]=nums2[:]             # we use slicing to slice the arrays and add them
        nums1.sort()
        return nums1
