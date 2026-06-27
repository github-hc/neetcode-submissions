class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts1={}
        counts2={}

        for i in s:
            counts1[i] = counts1.get(i,0) + 1

        for i in t:
            counts2[i] = counts2.get(i,0) + 1    
        
        return counts1==counts2