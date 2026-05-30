class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        position = {}
        for index in range(len(keyboard)):
            character = keyboard[index]
            position[character] = index
        
        current_position = 0
        total_time = 0

        for character in word:
            character_position = position[character]
            total_time += abs(current_position - character_position)
            current_position = character_position
        
        return total_time