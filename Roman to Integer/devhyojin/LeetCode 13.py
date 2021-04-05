class Solution:
    def romanToInt(self, s: str) -> int:
        sym_dic = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
        number = 0
        answer = 0
        for i in range(len(s)-1):
            if sym_dic[s[i]] >= sym_dic[s[i+1]:
                answer += dict[s[i]]
            else:
                answer -= dict[s[i]]
        return answer