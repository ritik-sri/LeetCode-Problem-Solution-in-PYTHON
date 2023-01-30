class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabets = string.ascii_lowercase
        key = key.replace(' ', '')
        new_key = ''
        ans = ''
        for letter in key: 
            if letter not in new_key:
                new_key+=letter
        for char in message:
            if char != ' ': 
                position_in_key = new_key.find(char)
                actual_char = alphabets[position_in_key]
                ans += actual_char
            elif char == ' ':
                ans += ' ' 
        return ans