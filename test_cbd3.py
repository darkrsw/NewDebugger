from CondBreakDebugger import CondBreakDebugger
from utils import next_inputs, clear_next_inputs
from hashtable import HashTable


def test_debug_htable():
    clear_next_inputs()
    next_inputs(["break key == 'mykey'", "continue", "set key = 'yourkey'", "continue", "set key = 'yourkey'", "continue"])

    with CondBreakDebugger() as debugged:
        hash_table = HashTable(50)
        hash_table.set_val('gfg@example.com', 'some value')
        hash_table.set_val('portal@example.com', 'some other value')
        hash_table.set_val('mykey', 'myvalue')
        hash_table.get_val('mykey')


    assert hash_table.get_val('mykey') == "No record found"
    assert hash_table.get_val('yourkey') == "myvalue"
