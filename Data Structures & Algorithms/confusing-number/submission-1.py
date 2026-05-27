class Solution:
    def confusingNumber(self, n: int) -> bool:
        valid_numbers = {
            "0": "0",
            "1": "1",
            "6": "9",
            "8": "8",
            "9": "6"
        }

        original_number = str(n)
        new_number = ""
        is_leading_zero = True

        for index in range(len(original_number) - 1, -1, -1):
            current_number = original_number[index]
            if current_number in valid_numbers:
                    new_number += valid_numbers[current_number]
            else:
                return False 

        if new_number == original_number:
            return False
        return True 