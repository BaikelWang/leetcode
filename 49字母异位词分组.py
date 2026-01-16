'''
Descripttion: 
version: 
Author: 王逸轩
Date: 2026-01-15 19:15:55
LastEditors: 王逸轩
LastEditTime: 2026-01-15 19:20:27
'''
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list) # 创建一个默认值为列表的字典
        for s in strs:  # 遍历每个字符串
            key = ''.join(sorted(s)) # 将字符串排序后作为键
            d[key].append(s) # 将字符串添加到对应键的列表中
        return list(d.values()) # 返回字典中所有值的列表
    
if __name__ == "__main__":
    sol = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(sol.groupAnagrams(strs))  # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]