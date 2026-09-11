class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        dict_need = {}
        dict_have = {}
        
        # Build frequency map of characters needed from t
        for char in t:  # FIX: was "for s in enumerate(t)" - shadowed input and enumerate returns tuples
            dict_need[char] = 1 + dict_need.get(char, 0)
            dict_have[char] = 0
        
        have = 0  # tracks how many unique chars have reached their required count
        need = len(dict_need)  # number of unique characters we need
        
        res = ""
        res_len = float("infinity")
        left = 0
        
        # Sliding window with right pointer
        for right in range(len(s)):
            char = s[right]
            
            # Add character to window
            if char in dict_need:
                dict_have[char] += 1
                # Only increment 'have' when we reach the required count
                if dict_have[char] == dict_need[char]:
                    have += 1
            
            # Shrink window from left when we have all characters
            while have == need:
                # Update result if current window is shorter
                if (right - left + 1) < res_len:
                    res = s[left:right + 1]
                    res_len = right - left + 1
                
                # Try to shrink from left
                if s[left] in dict_need:
                    dict_have[s[left]] -= 1
                    if dict_have[s[left]] < dict_need[s[left]]:
                        have -= 1
                left += 1
        
        return res