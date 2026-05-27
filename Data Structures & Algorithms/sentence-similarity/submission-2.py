class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        similar = {}
        def add_to_dict(key_word: str, value_word: str):
            if key_word in similar:
                similar[key_word].add(value_word)
            else:
                similar[key_word] = {value_word}
        
        if len(sentence1) != len(sentence2):
            return False
        
        for index in range(0, len(similarPairs)):
            word_one, word_two = similarPairs[index]
            add_to_dict(word_one, word_two)
            add_to_dict(word_two, word_one)
        
        for index in range(0, len(sentence1)):
            word_one = sentence1[index]
            word_two = sentence2[index]

            if word_one != word_two:
                if not(word_one in similar) or not(word_two in similar):
                    return False
                if not(word_one in similar[word_two]) or not(word_two in similar[word_one]):
                    return False
        return True
