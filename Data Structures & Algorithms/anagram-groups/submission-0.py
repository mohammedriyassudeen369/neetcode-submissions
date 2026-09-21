class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_hashmap = {}

        for i, word in enumerate(strs):
            sorted_word = tuple(sorted(word))
            if sorted_word not in anagram_hashmap:
                anagram_hashmap[sorted_word] = [strs[i]] 

            else:
                anagram_hashmap[sorted_word].append(strs[i])

        return_list = []
        for values in anagram_hashmap.values():
            return_list.append(values)
    
                
        return return_list



        

        
        