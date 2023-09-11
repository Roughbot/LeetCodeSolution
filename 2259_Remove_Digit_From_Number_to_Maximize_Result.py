class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        st = ""
        for i in range(len(number)):
            if number[i] == digit:
                temp = number[:i] + number[i+1:]  
                st = max(temp, st)  
        return st
