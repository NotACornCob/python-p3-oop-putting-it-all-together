#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
            
    # page_count property
    @property 
    def page_count(self):
        return self._page_count

    # page_count setter
    @page_count.setter 
    def page_count(self, page_count):
        '''prints "page_count must be an integer" if page_count is not an integer.'''
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")

TreasureIsland = Book("TreasureIsland", 333)