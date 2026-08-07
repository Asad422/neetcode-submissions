class Solution:
    def trap(self, height: List[int]) -> int:
        def scan(bars):
            totalWater = 0
            left = 0
            right = left + 1
            while (left < len(bars) and right < len(bars)):
                localWater = 0
                if (bars[left] > bars[right]):
                    right += 1
                else:
                    minBar = min(bars[left], bars[right])
                    for i in range(left + 1, right):
                        localWater += minBar - bars[i]
                    totalWater += localWater

                    left = right
                    right = left + 1

            return totalWater, left

        water, stopped = scan(height)
        water += scan(height[stopped:][::-1])[0]
        return water



                
                

        