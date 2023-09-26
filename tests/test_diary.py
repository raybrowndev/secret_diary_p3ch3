from lib.diary import Diary
import pytest



"""
read an entry with contents
return: string
"""

def test_read_method():
    my_diary = Diary("Today is september 26th!")
    result = my_diary.read()
    assert result == "Today is september 26th!"

"""
EDGE CASES 
"""


"""
read an empty diary
return: empty string
"""
def test_empty_contents():
    my_diary = Diary("")
    assert my_diary.contents == ""

"""
reading empty contents from diary
return: string 
"""

def test_empty_contents_exceprion():
    my_diary = Diary("")
    assert my_diary.read() == "My Diary is empty"

"""
type of contents invalid
return: raise excpetion 
"""

def test_invalid_input():
    with pytest.raises(Exception) as e:
        my_diary = Diary(12.34)
    error_message = str(e.value)
    assert error_message == "This is not a valid entry, try typing a word"




