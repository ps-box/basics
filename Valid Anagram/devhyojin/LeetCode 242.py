class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        leng = len(s)
        if len(s) != len(t):
            return False
        for i in range(leng):
            temp = s[i]
            print(temp)
            if temp in t:
                t = t.remove(temp)
                print(t)
        if t:
            return False
        else:
            return True