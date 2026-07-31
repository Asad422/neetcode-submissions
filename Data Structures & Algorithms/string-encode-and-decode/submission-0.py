class Solution:

    def encode(self, strs: List[str]) -> str:
        toReturn = ""
        for s in strs:
            toReturn += str(len(s)) + "#" + s
        return toReturn

    def decode(self, s: str) -> List[str]:
        toReturn = []
        i = 0
        while i < len(s):
            j = s.index("#", i)
            length = int(s[i:j])
            toReturn.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return toReturn 


        
