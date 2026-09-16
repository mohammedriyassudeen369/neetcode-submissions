class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hashmap_t = {}
        hashmap_s = {}

        # s_sorted_list = sorted(s)
        # t_sorted_list = sorted(t)

        for string in s:
            if string not in hashmap_s:
                hashmap_s[string] = 1
            
            else:
                hashmap_s[string] +=1

            # print(hashmap_s)

        for string in t:
            if string not in hashmap_t:
                hashmap_t[string] = 1
            
            else:
                hashmap_t[string] +=1

            # print(hashmap_t == hashmap_s)

        return (hashmap_t == hashmap_s)

        