class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        @cache
        def place(book_pos, cur_width, max_height):
            if book_pos == len(books):
                return 0
            width, height = books[book_pos]
            ans = height + place(book_pos + 1, width, height)  # new shelf
            if book_pos and cur_width + width <= shelfWidth:   # same shelf
                height_increase = max(0, height - max_height)
                ans = min(ans, height_increase + place(book_pos + 1, cur_width + width, max_height + height_increase))
            
            return ans
        
        return place(0, 0, 0)
            
