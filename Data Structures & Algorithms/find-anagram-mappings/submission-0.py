class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        occurrences = {}
        answers = []

        for index in range(len(nums2)):
            value = nums2[index]
            if value in occurrences:
                occurrences[value][0].append(index)
            else:
                occurrences[value] = [[index], 0]
        
        for number in nums1:
            index = occurrences[number][1]
            answers.append(occurrences[number][0][index])
            occurrences[number][1] += 1
        
        return answers