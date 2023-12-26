import pytest
from day20 import Conjunction, FlipFlop, Broadcaster

@pytest.fixture
def conjunction():
    c = Conjunction("con", [], [])
    return c

@pytest.fixture
def flipflop():
    ff = FlipFlop("flip", [])
    return ff

@pytest.fixture
def broadcaster():
    b = Broadcaster("broad", [])
    return b

# Conjunction tests
def test_is_all_input_high_fail(conjunction):
    conjunction.input_node_states = {
        "a":False,
        "b":True,
        "c":True
    }
    assert conjunction.is_all_input_high() == False

def test_is_all_input_high(conjunction):
    conjunction.input_node_states = {
        "a":True,
        "b":True,
        "c":True
    }
    assert conjunction.is_all_input_high() == True

def test_create_node_states_dict(conjunction):
    names = ["a", "b", "c"]
    states = conjunction.create_node_states_dict(names)
    expected_states = {
        "a":False,
        "b":False,
        "c":False
    }
    assert states == expected_states

# FlipFlop tests
def test_process_incoming_signals_high(flipflop):
    flipflop.incoming_signal = True
    flipflop.process_incoming_signals()
    assert flipflop.signal == None
    
def test_process_incoming_signals_off_low(flipflop):
    flipflop.is_on = False
    flipflop.incoming_signal = False
    flipflop.process_incoming_signals()
    assert flipflop.signal == True

def test_process_incoming_signals_on_low(flipflop):
    flipflop.is_on = True
    flipflop.incoming_signal = False
    flipflop.process_incoming_signals()
    assert flipflop.signal == False
    
def test_send_signal_high_energy(flipflop, conjunction):    
    flipflop.signal = True
    flipflop.output_nodes = [conjunction]
    conjunction.input_node_states = conjunction.create_node_states_dict(["flip"])
    receiving = flipflop.send_signals_and_return_receiving()
    assert conjunction.incoming_signal == True
    assert len(receiving) == 1

# Node tests
def test_send_signals_three_times(broadcaster, flipflop):
    broadcaster.output_nodes = [flipflop]
    receiving = broadcaster.send_signals_and_return_receiving()
    assert flipflop.signal == True
    assert len(receiving) == 1

    broadcaster.send_signals_and_return_receiving()
    assert flipflop.signal == False
    assert len(receiving) == 1

    broadcaster.send_signals_and_return_receiving()
    assert flipflop.signal == True
    assert len(receiving) == 1

    assert broadcaster.signals_sent[False] == 3

def test_send_signals_flipflops():
    a = FlipFlop("a", [])
    b = FlipFlop("b", [])
    c = FlipFlop("c", [])
    a.output_nodes = [b]
    b.output_nodes = [c]
    c.output_nodes = []
    broadcaster = Broadcaster("broadcaster", [a, b, c])

    assert a.signal == False
    assert b.signal == False
    assert c.signal == False

    receiving = broadcaster.send_signals_and_return_receiving()

    assert a.signal == True
    assert b.signal == True
    assert c.signal == True
    assert len(receiving) == 3

def test_send_signals_conjunction():
    inv = Conjunction("inv", ["a", "b", "c"], [])
    a = FlipFlop("a", [inv])
    b = FlipFlop("b", [inv])
    c = FlipFlop("c", [inv])

    assert inv.signal == False

    a_receiving = a.send_signals_and_return_receiving()
    b_receiving = b.send_signals_and_return_receiving()
    c_receiving = c.send_signals_and_return_receiving()
    
    assert inv.signal == False
    assert (len(a_receiving) + len(b_receiving) + len(c_receiving)) == 0
    
    a.signal = True
    b.signal = True
    c.signal = True
    a_receiving = a.send_signals_and_return_receiving()
    assert inv.signal == False
    b_receiving = b.send_signals_and_return_receiving()
    assert inv.signal == False
    c_receiving = c.send_signals_and_return_receiving()
    assert inv.signal == True
    assert (len(a_receiving) + len(b_receiving) + len(c_receiving)) == 3



