class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashtable = {}

        for i in range(len(nums)):

            val = target - nums[i]
            # print(val)

            if val not in hashtable:
                # print("iterate ,", nums[i])
                hashtable[nums[i]] = i
                # print(val, hashtable, nums[i])

            else:
                # print("else executed")
                # print([hashtable[val], i])
                return [hashtable[val], i]




        # nums[i] + nums[j] == target and i!=j:



        
        