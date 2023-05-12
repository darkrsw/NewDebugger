from CondBreakDebugger import CondBreakDebugger
from utils import next_inputs, clear_next_inputs
from sha256 import generate_hash
from md5 import md5_me


def test_debug_sha256():
    clear_next_inputs()
    next_inputs(["break a == 4216303719", "continue",  "set a = 1", "continue"])
    with CondBreakDebugger() as debugged:
        encoded = "debugggggggggggggggg".encode()
        hash = generate_hash(encoded).hex()

    assert hash == "6a09e6687787678f44c5a102776e322fc3a793acf083699d242ace90b010cee7"


def test_debug_md5():
    clear_next_inputs()
    next_inputs(["break d0 = 0x10325476", "continue",  "set d0 = 01333333", "continue"])
    with CondBreakDebugger() as debugged:
        encoded = "waytooloooooooooong".encode()
        hash = md5_me(encoded).hex()

    assert hash == "3931653962663531393065623166376238393234616332623538653635666133"
