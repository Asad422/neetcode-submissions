class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        slovarik = dict()

        for i in strs:
            sorted_i = ''.join(sorted(i))
            if sorted_i not in slovarik:
                slovarik[sorted_i] = [i]
            else:
                slovarik[sorted_i].append(i)

        return list(slovarik.values())           
        