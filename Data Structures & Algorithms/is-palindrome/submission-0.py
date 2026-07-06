class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = s.replace(" ","")
        n = len(clean_s)
        left = 0
        right = n-1


        while left < right:
            while left < right and not clean_s[left].isalnum():
                left += 1

            while left < right and not clean_s[right].isalnum():
                right -= 1

            if clean_s[left].lower() != clean_s[right].lower():
                return False

            left+=1
            right-=1
        
        return True

        
        