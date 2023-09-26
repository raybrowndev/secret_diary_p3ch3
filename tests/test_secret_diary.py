import pytest
from lib.secret_diary import SecretDiary
from unittest.mock import Mock 

"""
test lock status
return: TRUE
"""

def test_current_lock_status():
    fake_entry = Mock()
    my_private_diary = SecretDiary(fake_entry)
    assert my_private_diary.status == True


"""
test unlock diary
status == False
"""

def test_unlock_diary():
    fake_entry = Mock()
    my_private_diary = SecretDiary(fake_entry)
    my_private_diary.unlock()
    assert my_private_diary.status == False


"""
test UNLOCK > LOCK > UNLOCK 
status == FALSE 

"""

def test_unlock_and_lock_diary():
    fake_entry = Mock()
    my_private_diary = SecretDiary(fake_entry)
    my_private_diary.unlock()
    my_private_diary.lock()
    my_private_diary.unlock()
    assert my_private_diary.status == False


"""
test double lock
raise exception "This diary is already locked"
"""

def test_double_lock_diary():
    fake_entry = Mock()
    my_private_diary = SecretDiary(fake_entry)
    with pytest.raises(Exception) as e:
        my_private_diary.lock()
    error_message = str(e.value)
    assert error_message == "This diary is already locked"

"""
test double unlock
raise exception "This diary is already unlocked"
"""

def test_double_unlock_diary():
    fake_entry = Mock()
    my_private_diary = SecretDiary(fake_entry)
    with pytest.raises(Exception) as e:
        my_private_diary.unlock()
        my_private_diary.unlock()
    error_message = str(e.value)
    assert error_message == "This diary is already unlocked"
