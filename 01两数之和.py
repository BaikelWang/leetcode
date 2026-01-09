class Solution:
    def twoSum(self, nums, target: int):
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return (num_dict[complement], i)
            num_dict[num] = i
        return None

if __name__ == "__main__":
    sol = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(sol.twoSum(nums, target))  # Output: [0, 1]