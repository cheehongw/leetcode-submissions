class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # arrange the numbers by lexicographical order?
        # [2, 10]
        def cmp(a, b):
            str_a = str(a)
            str_b = str(b)

            a_b = str_a + str_b
            b_a = str_b + str_a

            if (a_b < b_a):
                return -1
            else:
                return 1

            # for i in range(min(len(str_a), len(str_b))):
            #     char_a = str_a[i]
            #     char_b = str_b[i]

            #     if char_a < char_b:
            #         return -1
            #     elif char_a > char_b:
            #         return 1
                
            # return -1 if len(str_a) < len(str_b) else 1



        nums.sort(reverse=True, key=functools.cmp_to_key(cmp))

        nums = [str(num) for num in nums]
        res = "".join(nums)

        return res.lstrip("0") or "0"
