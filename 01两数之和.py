'''
Descripttion: 
version: 
Author: 王逸轩
Date: 2026-01-08 13:42:24
LastEditors: 王逸轩
LastEditTime: 2026-01-15 19:16:32
'''
class Solution:
    def twoSum(self, nums, target: int):
        # 创建一个哈希表
        num_dict = {}
        for i, num in enumerate(nums): # num = nums[i]
            complement = target - num # 在哈希表中寻找 target - num
            if complement in num_dict:
                return (num_dict[complement], i) # 找到返回索引
            num_dict[num] = i # 将当前数字和索引存入哈希表
        return None

if __name__ == "__main__":
    sol = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(sol.twoSum(nums, target))  # Output: [0, 1]