class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        count  = {}

        for letter in s:
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1

        number_of_odds = 0

        for key in count:
            if count[key] % 2 != 0:
                number_of_odds += 1
                if number_of_odds > 1:
                    return False
        
        return True