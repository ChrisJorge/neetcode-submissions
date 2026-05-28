class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums.sort()
        seen = {}

        for index in range(len(nums) - 1, -1, -1):
            number = nums[index]
            if number in seen:
                seen[number] += 1
            else:
                seen[number] = 1
                if index < len(nums) - 1:
                    prev_number = nums[index + 1]
                    print(prev_number)
                    if seen[prev_number] == 1:
                        return prev_number
                    del seen[prev_number]

        for key in seen:
            if seen[key] == 1:
                return key
            else:
                return -1   
