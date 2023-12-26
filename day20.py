class Node:
    def __init__(self):
        self.signal = False # False = low, True = high
        self.incoming_signal = False
        self.incoming_signal_source = None
        self.signals_sent = {True: 0, False: 0}

    def send_signals_and_return_receiving(self):
        # Need for instance
        for node in self.output_nodes:
            node.incoming_signal = self.signal
            node.incoming_signal_source = self.name
            node.process_incoming_signals()
            self.signals_sent[self.signal] += 1
        return self.output_nodes


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

    def send_signals_and_return_receiving(self):
        if self.signal:
            return super().send_signals_and_return_receiving()
        else:
            return []


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


class SignalProcessor:
    def __init__(self):
        self.all_nodes = {}
    
    # Remember the button press is 1!
    # How does this terminate?
    def process_all_signals():
        broadcaster = Broadcaster("broadcaster", [])
        nodes_with_signals_to_send = [broadcaster]
        while nodes_with_signals_to_send:
            for next_node in nodes_with_signals_to_send:
                next_node.send_signals_and_return_receiving()
                nodes_with_signals_to_send.append(next_node.output_nodes)

    def instantiate_nodes(self, filepath):
        def get_name_and_nodes(row):
            name, other = row.split("-")
            name = name[1:].strip()
            nodes = other[1:].split(",")
            nodes = [node.strip() for node in nodes]
            return name, nodes

        # Needed since we can't reference instances as output nodes before they are created
        interim_node_structure = {}
        with open(filepath) as f:
            data = f.readlines()
            for row in data:
                name, node_names = get_name_and_nodes(row)        
                if "caster" in name:
                    node = Broadcaster(name="broadcaster", output_nodes=node_names)
                elif "%" in name:
                    node = FlipFlop(name=name, output_nodes=node_names)
                elif "&" in name:
                    conjunction_input_nodes = []
                    for row in data:
                        conj_input_name, conj_input_nodes = get_name_and_nodes(row)
                        if name in conj_input_nodes:
                            conjunction_input_nodes.append(conj_input_name)
                    node = Conjunction(name=name, output_nodes=node_names, input_node_names=conjunction_input_nodes)
                interim_node_structure[name] = node
            for n in interim_node_structure.keys():
                output_node_names = interim_node_structure[n].output_nodes
                output_node_instances = [interim_node_structure[output_name] for output_name in output_node_names]
                self.all_nodes[n] = interim_node_structure[n]
                self.all_nodes[n].output_nodes = output_node_instances


sp = SignalProcessor()
sp.instantiate_nodes("inputs/20.txt")
print()
#for a, b in sp.all_nodes.items():
#    print(a, b.name)