class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        hashmap = dict()
        toReturn = []
        for i in range(len(nums)):   
            leftSide = nums[:i]    
            rightSide = nums[i+1:]
            hashmap[i] = leftSide + rightSide
        for v in hashmap.values():
            localMultip = 1
            for x in v:
                localMultip *= x
            toReturn.append(localMultip)  

        return  toReturn    

                

        
        