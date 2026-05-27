class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for index in range(len(words)):
            current_word = words[index]
            
            for i in range(len(current_word)):
                row_character = current_word[i]

                if i < len(words):
                    column_word = words[i]

                    if index < len(column_word):
                        column_character = words[i][index]
                    else:
                        return False
                else:
                    return False 


                if row_character != column_character:
                    return False

        return True                      

