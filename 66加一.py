from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1): # 从后往前索引直到第0位: 长度、-1右开、步长减一
            if digits[i] < 9:
                digits[i] += 1  # 进位
                return digits
            digits[i] = 0  # 进位数字的右边数字都变成 0
        # digits 全是 9，加一后变成 100...00
        return [1] + digits # 在列表最前面加上 1
    
num = [1,2,3]
num_1 = [4,3,2,1]
num_2 = [9]
sol = Solution()
print(sol.plusOne(num))
print(sol.plusOne(num_1))
print(sol.plusOne(num_2))