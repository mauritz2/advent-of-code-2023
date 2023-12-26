class Node:
    def __init__(self):
        self.signal = False # False = low, True = high
        self.incoming_signal = False
        self.incoming_signal_source = None
        self.signals_sent = {True: 0, False: 0}

    def send_signals(self):
        for node in self.output_nodes:
            node.incoming_signal = self.signal
            node.incoming_signal_source = self.name
            node.process_incoming_signals()
            self.signals_sent[self.signal] += 1

class Broadcaster(Node):
    def __init__(self, name, output_nodes):
        super().__init__()
        self.name = name
        self.output_nodes = output_nodes

class FlipFlop(Node):
    """
    Flip-flop modules (prefix %) are either on or off; they are initially off. 
    If a flip-flop module receives a high pulse, it is ignored and nothing happens. 
    However, if a flip-flop module receives a low pulse, it flips between on and off. 
    If it was off, it turns on and sends a high pulse. If it was on, it turns off and sends a low pulse.
    """
    # off and gets low pulse --> turn on and send a high pulse
    # on and gets a low pulse --> turn off and send a low pulse
    # high pulse ignored

    def __init__(self, name, output_nodes):
        self.output_nodes = output_nodes
        self.name = name
        self.is_on = False
        super().__init__()

    def process_incoming_signals(self):
        if self.incoming_signal is True:
            self.signal = None
        elif self.incoming_signal is False:
            if self.is_on:
                self.signal = False
            else:
                self.signal = True
            self.is_on = not self.is_on
        else:
            raise ValueError("Incoming signal neither high nor low")

    
    def send_signals(self):
        # Change it to send_signals_and_return_receiving
        if self.signal:
            super().send_signals()

class Conjunction(Node):
    """ 
    Conjunction modules (prefix &) remember the type of the most recent pulse received from each of their connected input modules; 
    they initially default to remembering a low pulse for each input.
    When a pulse is received, the conjunction module first updates its memory for that input.
    Then, if it remembers high pulses for all inputs, 
    it sends a low pulse; otherwise, it sends a high pulse.
    """
    def __init__(self, name, input_node_names, output_nodes):
        self.name = name
        self.input_node_states = self.create_node_states_dict(input_node_names)
        self.output_nodes = output_nodes
        super().__init__()
    
    def create_node_states_dict(self, input_node_names):
        node_states = {name: False for name in input_node_names}
        return node_states

    def is_all_input_high(self):
        return all([node for node in self.input_node_states.values()])
    
    def process_incoming_signals(self):
        self.input_node_states[self.incoming_signal_source] = self.incoming_signal
        self.signal = self.is_all_input_high()

# Parser

# brodcaster
# a, b, c
# next_batch = [broadcaster]


# Remember the button press is 1!
class SignalProcessor:
    def __init__(self):
        pass
    
    def process_all_signals():
        broadcaster = Broadcaster("broadcaster", [])
        nodes_with_signals_to_send = [broadcaster]
        while nodes_with_signals_to_send:
            for next_node in nodes_with_signals_to_send:
                next_node.send_signals()
                nodes_with_signals_to_send.append(next_node.output_nodes)
