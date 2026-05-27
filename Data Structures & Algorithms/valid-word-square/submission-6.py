class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        longest_word_length = max(len(max(words, key = len)), len(words))
        matrix = [[None for _ in range(longest_word_length)] for _ in range(longest_word_length)]

        for index in range(len(words)):
            word = words[index]
            for letter in range(len(word)):
                matrix[index][letter] = word[letter]
        
        for index in range(len(words)):
            word = words[index]
            for letter in range(len(word)):
                row_character = matrix[index][letter]
                column_character = matrix[letter][index]

                if row_character != column_character:
                    return False
        return True