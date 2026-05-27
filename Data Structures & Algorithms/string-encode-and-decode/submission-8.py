class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''

        sequence = ""
        for word in strs:
            if not word:
                sequence += "EM"
                continue

            currentCharacter = word[0]
            count = 0

            for index in range(len(word)):
                if word[index] == currentCharacter:
                    count += 1
                else:
                    sequence += "N"
                    sequence += str(count)
                    sequence += "E"
                    sequence += currentCharacter
                    count = 1
                    currentCharacter = word[index]
                
                if index == len(word) - 1:
                    sequence += "N"
                    sequence += str(count)
                    sequence += "E"
                    sequence += currentCharacter
                    count = 1
                    currentCharacter = word[index]
            sequence += "EM"
        return sequence
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        print(s)
        ans = []
        index = 0
        string = ""
        while index < len(s):
            if s[index] == 'N':
                amount = ''
                index += 1
                while s[index] != 'E':
                    amount += s[index]
                    index += 1
                index += 1
                string += s[index] * int(amount)
            elif s[index] == 'E' and s[index + 1] == 'M':
                ans.append(string)
                string = ""
            index += 1
        return ans