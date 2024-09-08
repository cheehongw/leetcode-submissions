class Solution:
    def convertDateToBinary(self, date: str) -> str:
        items = date.split("-")
        yyyy = int(items[0])
        mm = int(items[1])
        dd = int(items[2])

        return "{0:b}-{1:b}-{2:b}".format(yyyy, mm, dd)
