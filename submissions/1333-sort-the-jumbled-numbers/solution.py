class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped = []

        for num in nums:
            mapped.append(self.mapp(num, mapping))

        res = sorted(zip(mapped, nums), key=lambda x : x[0])
        return [x[1] for x in res]
        




    def mapp(self, num, mapping):
        length = len(str(num))
        x = [0]*length

            
        for i in range(length -1, -1, -1):
            d = str(num)[i]
            md = mapping[int(d)]
            x[i] = str(md)

        return int(''.join(x))






            
        
