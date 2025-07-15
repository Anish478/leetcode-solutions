# Last updated: 7/15/2025, 5:50:46 PM
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j=0
        i =0
        while  i< len(nums1) and j < len(nums2):
            if nums1[i] == 0:
                nums1[i] = nums2[j]
                j+=1
                i+=1
            else:
                i+=1
        nums1.sort()
        
 


        