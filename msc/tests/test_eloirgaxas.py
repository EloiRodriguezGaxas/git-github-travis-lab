from msc.rot13 import rot13, rot13_char

def test_rot13_char_a():
    assert "n" == rot13_char("a"), "Unexpected character"