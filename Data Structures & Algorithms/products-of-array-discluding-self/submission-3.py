class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_list = [1] * n
        suffix_list = [1] * n
        final_list = [1] * n

        prefix = 1

        for i,v in enumerate(nums):
            print(i,v)
            prefix_list[i] = prefix
            prefix *= v

        suffix = 1

        for i,v in reversed(list(enumerate(nums))):
            suffix_list[i] = suffix
            suffix *= v

        for i,v in enumerate(prefix_list):
            final_list[i] = v * suffix_list[i]
        
        return final_list
