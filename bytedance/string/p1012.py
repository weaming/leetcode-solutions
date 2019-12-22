"https://leetcode-cn.com/explore/interview/card/bytedance/242/string/1012/"


class Solution:
    entry = 'lengthOfLongestSubstring'
    tests = [{'input': 'abcabcbb', 'answer': 3}, {'input': ' ', 'answer': 1}]

    def lengthOfLongestSubstring(self, s: str) -> int:
        rv = 0
        for i, j in self.all_start_end(s):
            x = s[i:j]
            if len(set(x)) == len(x) and len(x) > rv:
                rv = len(x)
        return rv

    def all_start_end(self, s):
        for i in range(len(s) + 1):
            for j in range(i, len(s) + 1):
                yield i, j
