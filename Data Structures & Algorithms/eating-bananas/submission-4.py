import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        maxValue = max(piles)
        minValue = 1
        minK = float('inf')
        while (minValue <= maxValue):
            localH = 0
            bph = ( minValue + maxValue ) // 2 
            for i in piles:
                localH += math.ceil(i/bph)
            if(localH > h):
                minValue = bph + 1
            else:
                maxValue =  bph - 1 
                if bph < minK:
                    minK = bph
        return minK
            














        





        