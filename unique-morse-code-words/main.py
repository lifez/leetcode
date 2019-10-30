class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        pattern = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result = set()
        for word in words:
            encode_string = ''
            for char in word:
                encode_string += pattern[ord(char)-97]
            result.add(encode_string)    
        return len(result)
