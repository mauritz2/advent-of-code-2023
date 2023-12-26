all_nodes = {}

class Node:
    def __init__(self):
        self.signal = False # False = low, True = high
        self.incoming_signal = None
        self.incoming_signal_source = None
        self.signals_sent = {True: 0, False: 0}

    def send_signals_and_return_receiving(self):
        # Need for instance
        for node_name in self.output_node_names:
            if node_name not in all_nodes.keys():
                # E.g., output node doesn't exist
                print(f"{node_name} doesn't exist!")
                continue
            node = all_nodes[node_name]
            node.incoming_signal = self.signal
            node.incoming_signal_source = self.name
            node.process_incoming_signals()
            self.signals_sent[self.signal] += 1
        return self.output_node_names


class Broadcaster(Node):
    def __init__(self, name, output_node_names):
        super().__init__()
        self.name = name
        self.output_node_names = output_node_names
    
    def process_incoming_signals(self):
        pass


class FlipFlop(Node):
    """
    Flip-flop modules (prefix %) are either on or off; they are initially off. 
    If a flip-flop module receives a high pulse, it is ignored and nothing happens. 
    However, if a flip-flop module receives a low pulse, it flips between on and off. 
    If it was off, it turns on and sends a high pulse. If it was on, it turns off and sends a low pulse.
    """
    def __init__(self, name, output_node_names):
        self.output_node_names = output_node_names
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
    def __init__(self, name, input_node_names, output_node_names):
        self.name = name
        self.input_node_states = self.create_node_states_dict(input_node_names)
        self.output_node_names = output_node_names
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
    def process_all_signals():
        node_names_with_signals_to_send = ["broadcaster"]
        all_nodes["broadcaster"].signals_sent[False] += 1 #button press
        while node_names_with_signals_to_send:
            next_node_name = node_names_with_signals_to_send.pop(0)
            if next_node_name not in all_nodes.keys():
                print(f"{next_node_name} doesn't exist")
                continue
            all_nodes[next_node_name].process_incoming_signals()
            nodes_names_receiving_signals = all_nodes[next_node_name].send_signals_and_return_receiving()
            # Why does b not send anything to c?
            for new_node_name in nodes_names_receiving_signals:
                node_names_with_signals_to_send.append(new_node_name)
        # Remember the button press is 1!

    def count_signals_sent():
        low_sent = sum([node.signals_sent[0] for node in all_nodes.values()]) # 8
        high_sent = sum([node.signals_sent[1] for node in all_nodes.values()]) # 4
        return low_sent * high_sent

def get_name_and_nodes(row):
    name, other = row.split("-")
    name = name.strip()
    nodes = other[1:].split(",")
    nodes = [node.strip() for node in nodes]
    return name, nodes

with open("inputs/20.txt") as f:
    data = f.readlines()
    for row in data:
        name, node_names = get_name_and_nodes(row)        
        if "%" in name:
            name = name[1:]
            node = FlipFlop(name=name, output_node_names=node_names)
        elif "&" in name:
            name = name[1:]
            conjunction_input_nodes = []
            for row in data:
                conj_input_name, conj_input_nodes = get_name_and_nodes(row)
                if name in conj_input_nodes:
                    conjunction_input_nodes.append(conj_input_name)
            node = Conjunction(name=name, output_node_names=node_names, input_node_names=conjunction_input_nodes)
        elif "caster" in name:
            node = Broadcaster(name=name, output_node_names=node_names)
        else:
            raise ValueError("No match to other nodes")
        all_nodes[name] = node


#for _ in range(1000):
SignalProcessor.process_all_signals()

signals_sent = SignalProcessor.count_signals_sent()
print(signals_sent)