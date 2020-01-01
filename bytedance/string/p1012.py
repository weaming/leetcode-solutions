"""
https://leetcode-cn.com/explore/interview/card/bytedance/242/string/1012/
https://leetcode-cn.com/articles/longest-substring-without-repeating-characters/
    滑动窗口：滑动窗口是数组/字符串问题中常用的抽象概念。
    窗口通常是在数组/字符串中由开始和结束索引定义的一系列元素的集合，即 [i, j)（左闭，右开）。
    而滑动窗口是可以将两个边界向某一方向“滑动”的窗口。
    例如，我们将 [i, j)向右滑动 1 个元素，则它将变为 [i+1, j+1)（左闭，右开）。
"""


class Solution:
    entry = 'lengthOfLongestSubstring'
    tests = [{'input': 'abcabcbb', 'answer': 3}, {'input': ' ', 'answer': 1}]

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Using HashMap as optimized sliding window.
        The HashMap has the ability to remember more information.
        O(n)
        """
        i, j = 0, 0
        n = len(s)
        cs = {}
        rv = 0
        while i < n and j < n:
            if s[j] in cs:
                i = max(i, cs[s[j]])

            cs[s[j]] = j + 1  # next index will be used to update variable i
            j += 1
            rv = max(rv, j - i)
        return rv

    def lengthOfLongestSubstring2(self, s: str) -> int:
        """
        Using Set as sliding window.
        O(2n)
        """
        i, j = 0, 0
        n = len(s)
        cs = set()
        rv = 0
        while i < n and j < n:
            if s[j] not in cs:
                cs.add(s[j])
                j += 1
                rv = max(rv, j - i)
            else:
                cs.remove(s[i])
                i += 1
        return rv

    def lengthOfLongestSubstring1(self, s: str) -> int:
        """
        Timeout for long string.
        """
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
