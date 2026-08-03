class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        toReturn = []
        sortedNums = sorted(nums)
        [-4,-1,-1,0,1,2]
        for i in range(len(sortedNums)):
            if i > 0 and sortedNums[i] == sortedNums[i-1]:
                continue
            toFind = -sortedNums[i]
            left = i+1
            right = len(sortedNums)-1
            while(left< right):
                if(sortedNums[left] + sortedNums[right] > toFind):
                    right -= 1 
                elif(sortedNums[left] + sortedNums[right] < toFind):
                    left += 1
                else:
                    toReturn.append([sortedNums[i], sortedNums[left], sortedNums[right]])
                    left += 1
                    right -= 1
                    while left < right and sortedNums[left] == sortedNums[left-1]:
                        left += 1
                    while left < right and sortedNums[right] == sortedNums[right+1]:
                        right -= 1

        return toReturn      
            

        

            

        