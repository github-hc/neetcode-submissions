class Solution:
    def find(self, nums: List[int], target: int, l:int, r:int):
        
        if l>r:
            return -1
        mid = (l + r) // 2

        if nums[mid]==target:
            return mid

        if target > nums[mid]:
            return self.find(nums, target, mid+1, r)

        else: 
            return self.find(nums, target, l, mid-1)    

     
    def search(self, nums: List[int], target: int) -> int:
        return self.find(nums, target, 0, len(nums)-1)