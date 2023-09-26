# File: lib/diary.py

class Diary:
    def __init__(self, contents):
        if type(contents) == str:
            self.contents = contents
        else: 
            raise Exception("This is not a valid entry, try typing a word")


    def read(self):
        if self.contents == "": 
            return "My Diary is empty"
        else:
            return self.contents
