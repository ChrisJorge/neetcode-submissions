class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        count  = {}
        number_of_odds = 0

        for letter in s:
            if letter in count:
                count[letter] += 1
                if count[letter] % 2 == 0:
                    number_of_odds -= 1
                else:
                    number_of_odds += 1
            else:
                count[letter] = 1
                number_of_odds += 1
        
        return number_of_odds < 2

