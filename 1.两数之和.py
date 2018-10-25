class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, value in enumerate(nums):
            s = target - value 
            for j in range(i+1, len(nums)):
                if nums[j] == s:
                    return [i, j]
        return [] 


if __name__ == "__main__":
    nums = [3,3]
    target = 6
    print(Solution().twoSum(nums=nums, target=target))