class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        
        for num in nums:
            counts[num] = counts.get(num,0) + 1

        if any(count > 1 for count in counts.values()):
            return True
        else:
            return False
        