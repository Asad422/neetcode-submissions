class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False

        firstdict = dict()
        seconddict = dict()
        
        for i in s:
            if i not in firstdict:
                firstdict[i] =1

            else:
                firstdict[i] +=1


        for i in t:
            if i not in seconddict:
                seconddict[i] =1

            else:
                seconddict[i] +=1  

        for k,v in firstdict.items():
            if k not in seconddict:
                return False
            if firstdict[k] != seconddict[k]:  
                return False

        return True           



