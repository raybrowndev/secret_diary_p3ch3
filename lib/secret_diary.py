# File: lib/secret_diary.py
from lib.diary import *
import pytest 

class SecretDiary:
    def __init__(self, entry):
        self.status = True
        # # diary = isinstance(entry, Diary)
        if not isinstance(entry, Diary):
            raise Exception("Enter contents in diary class")
        else:
            self.diary = entry
            


    def read(self):
        if self.status == True:
            return "Go away!"
        else:
            return self.diary
        # Raises the error "Go away!" if the diary is locked
        # Returns the diary's contents if the diary is unlocked
        # The diary starts off locked


    def lock(self):
        if self.status == True:
            raise Exception("This diary is already locked")
        else:
            self.status = True

    def unlock(self):
        if self.status == False:
            raise Exception("This diary is already unlocked") 
        else:
            self.status = False