class Solution:
    def removeDuplicates(self, nums):
        nums = list(set(nums))
        return len(nums)

# class Solution:
#     def removeDuplicates(self, nums):
#         i = 0
#         while(i<(len(nums)-1)):
#             if(nums[i] == nums[i+1]):
#                 del nums[i+1]
#                 continue
#             else:
#                 i += 1
#         return len(nums)

if __name__ == "__main__":
    s = Solution()
    print(list(set([1,1,2])))

