"""
https://leetcode-cn.com/explore/interview/card/bytedance/242/string/1014/
"""
from typing import List


class Solution:
    entry = 'longestCommonPrefix'
    tests = [
        {'input': ["flower", "flow", "flight"], 'answer': 'fl'},
        {'input': ["dog", "racecar", "car"], 'answer': ''},
    ]

    def longestCommonPrefix(self, strs: List[str]) -> str:
        columns = list(zip(*[list(x) for x in strs]))
        rv = []
        for c in columns:
            # if all chars with same index from all rows are same
            if len(set(c)) == 1:
                rv.append(c[0])
            else:
                break
        return ''.join(rv)
