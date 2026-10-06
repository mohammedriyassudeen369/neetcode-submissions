class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        total_product = 1
        prod = []
        count = 0
        for num in nums:
            if num!=0:
                total_product *= num
            else:
                count +=1

            # else:
            #     total_product = 1

        # FINDING THE COUNT OF ZEROES AS AN EDGE CASE...if ONE ZERO THEN OUPUT WILL BE Input: nums = [-1,0,1,2,3] Output: [0,-6,0,0,0]..MORE THAN ONE ALL THE LISTS BECOMES ZERO
        if count == 0:
            # print(total_product)
            # USe division method and distribute a list
            for num in nums:
                val =int(total_product / num )
                prod.append(val)
            # print(prod)
        elif count == 1:
            # pass
            # print(f"count  1 executed total product {total_product}")
            for i, num in enumerate(nums):
                if num == 0:
                    print(i, prod)
                    prod.append(total_product)
                else:
                    prod.append(0)
        else:
            total_product = 0
            for num in nums:
                prod.append(0)
            # print(f"count > 1 executed total product {total_product}")

        return prod


      

                

        