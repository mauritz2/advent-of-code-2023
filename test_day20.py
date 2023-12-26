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
    flipflop.send_signals()
    assert conjunction.incoming_signal == True

# Node tests
def test_send_signals_three_times(broadcaster, flipflop):
    broadcaster.output_nodes = [flipflop]
    broadcaster.send_signals()
    assert flipflop.signal == True

    broadcaster.send_signals()
    assert flipflop.signal == False

    broadcaster.send_signals()
    assert flipflop.signal == True

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

    broadcaster.send_signals()

    assert a.signal == True
    assert b.signal == True
    assert c.signal == True

def test_send_signals_conjunction():
    inv = Conjunction("inv", ["a", "b", "c"], [])
    a = FlipFlop("a", [inv])
    b = FlipFlop("b", [inv])
    c = FlipFlop("c", [inv])

    assert inv.signal == False

    a.send_signals()
    b.send_signals()
    c.send_signals()
    
    assert inv.signal == False
    
    a.signal = True
    b.signal = True
    c.signal = True
    a.send_signals()
    assert inv.signal == False
    b.send_signals()
    assert inv.signal == False
    c.send_signals()
    assert inv.signal == True



