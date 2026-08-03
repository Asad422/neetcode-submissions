class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #  i - bar
        #  heights[i] - height of an i bar

        globalMaximum = 0

        left = 0

        right = len(heights) - 1
        [1,7,2,5,4,7,3,6]
        while(left < right):
            stolb = min(heights[left],heights[right])
            localMaximum = (right - left) * stolb
            if(localMaximum > globalMaximum):
                globalMaximum = localMaximum
            if(heights[left] <= heights[right]):
                left+=1
            elif(heights[left] > heights[right]):
                right-=1    
           
                
        return globalMaximum     


            



    