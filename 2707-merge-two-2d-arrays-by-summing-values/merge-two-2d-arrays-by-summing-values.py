class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        merged = {}
        for id, val in nums1:
            merged[id] = merged.get(id, 0) + val
        for id, val in nums2:
            merged[id] = merged.get(id, 0) + val

    
        result = sorted([[id, val] for id, val in merged.items()])
        return result