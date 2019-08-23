class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashTable = {}
        
        for i in range(0,len(nums)):
            
            targetMinusNums = target - nums[i]
            
            if targetMinusNums in hashTable:
                return[hashTable[targetMinusNums],i]
                break
            hashTable[nums[i]] = i
        return[] 