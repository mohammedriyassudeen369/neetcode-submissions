class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_str = ""

        for st in strs:
            encoded_str += str(len(st)) + '#' + st

        # print(encoded_str)
        return encoded_str 

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0

        while i < len(s):

            # Step 1: Find the delimiter
            j = s.find('#', i)

            # Step 2: Extract the length
            length = int(s[i:j])

            # Step 3: Find the starting position of the actual string
            start = j + 1

            # Step 4: Calculate the ending position
            end = start + length

            # Step 5: Extract the original string
            res.append(s[start:end])

            # Step 6: Move to the next encoded string
            i = end

        return res
