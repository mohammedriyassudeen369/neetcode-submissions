class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequent_hashmap = {}

        for ele in nums:
            if ele not in frequent_hashmap:
                frequent_hashmap[ele] = 1
                # print(frequent_hashmap)

            else:
                frequent_hashmap[ele] +=1
                # print(frequent_hashmap)

        sorted_frquency_hashmap_values = sorted(frequent_hashmap, key=frequent_hashmap.get, reverse = True)

        # print(sorted_frquency_hashmap_values)

        res_list = sorted_frquency_hashmap_values[:k]

        return res_list

        


        