# File: lib/secret_diary.py

class SecretDiary:
    def __init__(self, diary):
        self.diary = diary 
        self.status = True

    def read(self):
        # Raises the error "Go away!" if the diary is locked
        # Returns the diary's contents if the diary is unlocked
        # The diary starts off locked
        pass

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