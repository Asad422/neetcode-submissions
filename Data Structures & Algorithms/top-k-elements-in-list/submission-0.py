class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        for i in nums:
            if i not in counter:
                counter[i] = 1
            else:
                counter[i] +=1

        sorted_counter = sorted(counter.items(), key=lambda x: x[1])
        return [pair[0] for pair in sorted_counter[len(sorted_counter) - k:]]

    



            