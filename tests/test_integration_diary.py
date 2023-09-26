from lib.secret_diary import *
from unittest.mock import Mock
import pytest 
"""
read with one entry with diary lock ==> "Go away!" type str
"""

def test_one_entry_diary_lock():
    fake_entry = Mock(spec=Diary)
    my_private_diary = SecretDiary(fake_entry)
    assert my_private_diary.read() == "Go away!"

"""
read with one entry with diary unlock ==> contents diary type
"""

def test_one_entry_diary_unlock():
    fake_entry = Mock(spec=Diary)
    my_private_diary = SecretDiary(fake_entry)
    my_private_diary.unlock()
    assert my_private_diary.read() == fake_entry
"""
read the diary unlock (status == False, read returns+ diary contents), 
    lock it (status == True),
        read again ==> "Go away!" type str
"""
def test_one_entry_diary_unlock_locked_read():
    fake_entry = Mock(spec=Diary)
    my_private_diary = SecretDiary(fake_entry)
    my_private_diary.unlock()
    assert my_private_diary.status == False
    assert my_private_diary.read() == fake_entry
    my_private_diary.lock()
    assert my_private_diary.status == True
    assert my_private_diary.read() == "Go away!"

"""
wrong type of entry ==> raise Exception "Enter contents in diary class"
"""
def test_entry_type_invalid():
    with pytest.raises(Exception) as e:
        my_private_diary = SecretDiary("fake_entry")
    error_message = str(e.value)
    assert error_message == "Enter contents in diary class"