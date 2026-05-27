class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = {}
        for number in nums:
            if number in count:
                count[number] += 1
            else:
                count[number] = 1
        
        ans = []
        for key in count:
            if count[key] == 1:
                ans.append(key)

        if not(ans):
            return -1
        ans.sort()
        return ans[-1]