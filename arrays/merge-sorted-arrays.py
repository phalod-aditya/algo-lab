# https://leetcode.com/problems/merge-sorted-array/description/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # clean up nums1. remove trailing 0s
        nums1[:] = nums1[:m]
        # print(nums1)

        # merge & sort
        merged = nums1 + nums2

        merged = sorted(merged)

        # print(merged)

        # re-write nums1
        nums1[:] = merged

        return
