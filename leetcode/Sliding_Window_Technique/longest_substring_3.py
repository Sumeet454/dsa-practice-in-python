# Longest Substring Without Repeating Characters

class Solution:
    def longestSubstring(self,s:str):
        n= len(s)
        char_index = {}
        start = 0
        max_length = 0
        longest_substring=""
        for i in range(n):
            if s[i] in char_index and char_index[s[i]]>=start:
                start = char_index[s[i]]+1
            char_index[s[i]]=i
            if i-start+1 > max_length:
                max_length = i-start+1
                longest_substring = s[start:i+1]
        return max_length, longest_substring
object = Solution()
print(object.longestSubstring("abcabcbb"))