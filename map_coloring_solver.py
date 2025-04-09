import random
import copy
from datetime import datetime

# Global variables
backtracks = 0
color_names = {
    'R': 'Red',
    'G': 'Green',
    'B': 'Blue',
    'Y': 'Yellow',
    'P': 'Purple'
}

# Dictionary containing the states of the USA and Australia, along with their neighboring states.
map_data = {
    'USA': {
        'states': [
            'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California',
            'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia',
            'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas',
            'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts',
            'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana',
            'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico',
            'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma',
            'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',
            'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
            'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'
        ],
        'neighbors': {
            'Alabama': ['Florida', 'Georgia', 'Mississippi', 'Tennessee'],
            'Alaska': [],
            'Arizona':
            ['California', 'Colorado', 'New Mexico', 'Nevada', 'Utah'],
            'Arkansas': [
                'Louisiana', 'Missouri', 'Mississippi', 'Oklahoma',
                'Tennessee', 'Texas'
            ],
            'California': ['Arizona', 'Nevada', 'Oregon'],
            'Colorado': [
                'Arizona', 'Kansas', 'Nebraska', 'New Mexico', 'Oklahoma',
                'Utah', 'Wyoming'
            ],
            'Connecticut': ['Massachusetts', 'New York', 'Rhode Island'],
            'Delaware': ['Maryland', 'New Jersey', 'Pennsylvania'],
            'Florida': ['Alabama', 'Georgia'],
            'Georgia': [
                'Alabama', 'Florida', 'North Carolina', 'South Carolina',
                'Tennessee'
            ],
            'Hawaii': [],
            'Idaho':
            ['Montana', 'Nevada', 'Oregon', 'Utah', 'Washington', 'Wyoming'],
            'Illinois': [
                'Indiana', 'Iowa', 'Kentucky', 'Michigan', 'Missouri',
                'Wisconsin'
            ],
            'Indiana': ['Illinois', 'Kentucky', 'Michigan', 'Ohio'],
            'Iowa': [
                'Illinois', 'Minnesota', 'Missouri', 'Nebraska',
                'South Dakota', 'Wisconsin'
            ],
            'Kansas': ['Colorado', 'Missouri', 'Nebraska', 'Oklahoma'],
            'Kentucky': [
                'Illinois', 'Indiana', 'Missouri', 'Ohio', 'Tennessee',
                'Virginia', 'West Virginia'
            ],
            'Louisiana': ['Arkansas', 'Mississippi', 'Texas'],
            'Maine': ['New Hampshire'],
            'Maryland':
            ['Delaware', 'Pennsylvania', 'Virginia', 'West Virginia'],
            'Massachusetts': [
                'Connecticut', 'New Hampshire', 'New York', 'Rhode Island',
                'Vermont'
            ],
            'Michigan':
            ['Illinois', 'Indiana', 'Minnesota', 'Ohio', 'Wisconsin'],
            'Minnesota':
            ['Iowa', 'Michigan', 'North Dakota', 'South Dakota', 'Wisconsin'],
            'Mississippi': ['Alabama', 'Arkansas', 'Louisiana', 'Tennessee'],
            'Missouri': [
                'Arkansas', 'Illinois', 'Iowa', 'Kansas', 'Kentucky',
                'Nebraska', 'Oklahoma', 'Tennessee'
            ],
            'Montana': ['Idaho', 'North Dakota', 'South Dakota', 'Wyoming'],
            'Nebraska': [
                'Colorado', 'Iowa', 'Kansas', 'Missouri', 'South Dakota',
                'Wyoming'
            ],
            'Nevada': ['Arizona', 'California', 'Idaho', 'Oregon', 'Utah'],
            'New Hampshire': ['Maine', 'Massachusetts', 'Vermont'],
            'New Jersey': ['Delaware', 'New York', 'Pennsylvania'],
            'New Mexico': ['Arizona', 'Colorado', 'Oklahoma', 'Texas', 'Utah'],
            'New York': [
                'Connecticut', 'Massachusetts', 'New Jersey', 'Pennsylvania',
                'Rhode Island', 'Vermont'
            ],
            'North Carolina':
            ['Georgia', 'South Carolina', 'Tennessee', 'Virginia'],
            'North Dakota': ['Minnesota', 'Montana', 'South Dakota'],
            'Ohio': [
                'Indiana', 'Kentucky', 'Michigan', 'Pennsylvania',
                'West Virginia'
            ],
            'Oklahoma': [
                'Arkansas', 'Colorado', 'Kansas', 'Missouri', 'New Mexico',
                'Texas'
            ],
            'Oregon': ['California', 'Idaho', 'Nevada', 'Washington'],
            'Pennsylvania': [
                'Delaware', 'Maryland', 'New Jersey', 'New York', 'Ohio',
                'West Virginia'
            ],
            'Rhode Island': ['Connecticut', 'Massachusetts', 'New York'],
            'South Carolina': ['Georgia', 'North Carolina'],
            'South Dakota': [
                'Iowa', 'Minnesota', 'Montana', 'Nebraska', 'North Dakota',
                'Wyoming'
            ],
            'Tennessee': [
                'Alabama', 'Arkansas', 'Georgia', 'Kentucky', 'Mississippi',
                'Missouri', 'North Carolina', 'Virginia'
            ],
            'Texas': ['Arkansas', 'Louisiana', 'New Mexico', 'Oklahoma'],
            'Utah': [
                'Arizona', 'Colorado', 'Idaho', 'Nevada', 'New Mexico',
                'Wyoming'
            ],
            'Vermont': ['Massachusetts', 'New Hampshire', 'New York'],
            'Virginia': [
                'Kentucky', 'Maryland', 'North Carolina', 'Tennessee',
                'West Virginia'
            ],
            'Washington': ['Idaho', 'Oregon'],
            'West Virginia':
            ['Kentucky', 'Maryland', 'Ohio', 'Pennsylvania', 'Virginia'],
            'Wisconsin': ['Illinois', 'Iowa', 'Michigan', 'Minnesota'],
            'Wyoming': [
                'Colorado', 'Idaho', 'Montana', 'Nebraska', 'South Dakota',
                'Utah'
            ]
        }
    },
    'Australia': {
        'states': [
            'Western Australia', 'Northern Territory', 'South Australia',
            'Queensland', 'New South Wales', 'Victoria', 'Tasmania'
        ],
        'neighbors': {
            'Western Australia': ['Northern Territory', 'South Australia'],
            'Northern Territory':
            ['Western Australia', 'South Australia', 'Queensland'],
            'South Australia': [
                'Western Australia', 'Northern Territory', 'Queensland',
                'New South Wales', 'Victoria'
            ],
            'Queensland':
            ['Northern Territory', 'South Australia', 'New South Wales'],
            'New South Wales': ['Queensland', 'Victoria', 'South Australia'],
            'Victoria': ['New South Wales', 'South Australia'],
            'Tasmania': []
        }
    }
}


# Prompts the user for input and validates it within the given range.
def get_valid_input(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"Please enter a number between {min_val} and {max_val}")
        except ValueError:
            print("Invalid input. Please enter a number.")


# Initializes the color for each state as uncolored.
def initialize_colors(states):
    return {state: None for state in states}


# Initializes the possible color options for each state.
def initialize_domain(states, num_colors):
    colors = list(color_names.keys())[:num_colors]
    return {state: copy.deepcopy(colors) for state in states}


# Calculates the chromatic number (minimum number of colors required).
def get_chromatic_number(states, neighbors):
    for num_colors in range(1, 6):
        temp_states = copy.deepcopy(states)
        colors = initialize_colors(states)
        domain = initialize_domain(states, num_colors)
        global backtracks
        backtracks = 0
        if backtrack(temp_states, neighbors, colors, domain, False) == "Success":
            return num_colors
    return 5


# Selects the state with the minimum remaining values (MRV).
def mrv_heuristic(states, domain, neighbors):
    states.sort(key=lambda x: (len(domain[x]), -len(neighbors[x])))
    return states[0]


# Orders colors for a state by the least-constraining value (LCV).
def lcv_heuristic(state, domain, neighbors):
    color_counts = []
    for color in domain[state]:
        count = sum(1 for neighbor in neighbors[state] if color in domain[neighbor])
        color_counts.append((color, count))
    color_counts.sort(key=lambda x: x[1])
    return [color for color, _ in color_counts]


# Reduces the domains of neighboring states after a color is assigned.
def reduce_domains(state, color, neighbors, colors, domain):
    for neighbor in neighbors[state]:
        if colors[neighbor] is None and color in domain[neighbor]:
            domain[neighbor].remove(color)


# Checks if a state has only one color available in its domain.
def check_singleton(state, neighbors, colors, domain):
    for neighbor in neighbors[state]:
        if colors[neighbor] is None and len(domain[neighbor]) == 1:
            return True
    return False


# Propagates the singleton property to neighboring states, reducing their domains.
def propagate_singleton(state, neighbors, colors, domain):
    queue = [state]
    while queue:
        current = queue.pop(0)
        if colors[current] is not None:
            continue

        if len(domain[current]) == 1:
            color = domain[current][0]
            colors[current] = color
            for neighbor in neighbors[current]:
                if color in domain[neighbor]:
                    domain[neighbor].remove(color)
                    if len(domain[neighbor]) == 1:
                        queue.append(neighbor)
                    elif len(domain[neighbor]) == 0:
                        return False
    return True


# Solves the problem using the backtracking algorithm.
def backtrack(states, neighbors, colors, domain, use_heuristics):
    global backtracks

    if all(color is not None for color in colors.values()):
        return "Success"

    current_state = mrv_heuristic(states, domain, neighbors) if use_heuristics else states[0]
    color_order = lcv_heuristic(
        current_state, domain,
        neighbors) if use_heuristics else domain[current_state]

    for color in color_order:
        if all(color != colors[neighbor]
               for neighbor in neighbors[current_state]
               if colors[neighbor] is not None):
            colors[current_state] = color
            states.remove(current_state)

            result = backtrack(states, neighbors, colors, domain, use_heuristics)
            if result == "Success":
                return "Success"

            colors[current_state] = None
            states.append(current_state)

    if colors[current_state] is None:
        backtracks += 1
        return "Failure"


# Performs forward checking to prune invalid color assignments.
def forward_check(states, neighbors, colors, domain, use_heuristics):
    global backtracks

    if all(color is not None for color in colors.values()):
        return "Success"

    current_state = mrv_heuristic(states, domain, neighbors) if use_heuristics else states[0]
    color_order = lcv_heuristic(
        current_state, domain,
        neighbors) if use_heuristics else domain[current_state]

    for color in color_order:
        if all(color != colors[neighbor]
               for neighbor in neighbors[current_state]
               if colors[neighbor] is not None):
            colors[current_state] = color
            states.remove(current_state)

            old_domain = copy.deepcopy(domain)
            reduce_domains(current_state, color, neighbors, colors, domain)

            result = forward_check(states, neighbors, colors, domain, use_heuristics)
            if result == "Success":
                return "Success"

            domain = old_domain
            colors[current_state] = None
            states.append(current_state)

    if colors[current_state] is None:
        backtracks += 1
        return "Failure"


# Applies forward checking with singleton propagation to reduce domains.
def forward_check_with_singleton(states, neighbors, colors, domain, use_heuristics):
    global backtracks

    if all(color is not None for color in colors.values()):
        return "Success"

    current_state = mrv_heuristic(states, domain, neighbors) if use_heuristics else states[0]
    color_order = lcv_heuristic(
        current_state, domain,
        neighbors) if use_heuristics else domain[current_state]

    for color in color_order:
        if all(color != colors[neighbor]
               for neighbor in neighbors[current_state]
               if colors[neighbor] is not None):
            colors[current_state] = color
            states.remove(current_state)

            old_domain = copy.deepcopy(domain)
            reduce_domains(current_state, color, neighbors, colors, domain)

            if check_singleton(current_state, neighbors, colors, domain):
                if not propagate_singleton(current_state, neighbors, colors, domain):
                    colors[current_state] = None
                    states.append(current_state)
                    domain = old_domain
                    continue

            result = forward_check_with_singleton(states, neighbors, colors, domain, use_heuristics)
            if result == "Success":
                return "Success"

            domain = old_domain
            colors[current_state] = None
            states.append(current_state)

    if colors[current_state] is None:
        backtracks += 1
        return "Failure"


# Prints the final solution in a nice format
def print_solution(colors, min_colors, time_elapsed):
    print("\n----------------------------------------------------")
    print(f"Map Coloring Solution (Minimum Colors Required: {min_colors}):")
    print("----------------------------------------------------\n")

    # Group by color
    color_groups = {}
    for state, color in colors.items():
        if color not in color_groups:
            color_groups[color] = []
        color_groups[color].append(state)

    for color, states in color_groups.items():
        print(f"{color_names[color]}:")
        for state in sorted(states):
            print(f"  {state}")
        print()

    print(f"Number of Backtracks: {backtracks}")
    print(f"Time Required to Compute: {time_elapsed:.2f} ms\n")


# Main function
def main():
    global backtracks

    print("\n----------------------------------------------------")
    print("Map Coloring Solver")
    print("----------------------------------------------------")

    print("\nSelect a map:")
    for i, map_name in enumerate(map_data.keys(), 1):
        print(f"{i}. {map_name}")
    map_choice = get_valid_input("\nEnter Choice (1-2): ", 1, 2) - 1
    map_name = list(map_data.keys())[map_choice]
    states = map_data[map_name]['states']
    neighbors = map_data[map_name]['neighbors']

    print("\nUse heuristics?")
    print("1. Without Heuristics")
    print("2. With Heuristics")
    use_heuristics = get_valid_input("\nEnter Choice (1-2): ", 1, 2) == 2

    print("\nSelect Method:")
    print("1. Depth-first search only")
    print("2. Depth-first search + forward checking")
    print("3. Depth-first search + forward checking + singleton propagation")
    algorithm = get_valid_input("\nEnter Choice (1-3): ", 1, 3)

    print("\nSolving...")
    start_time = datetime.now()

    # Find minimum number of colors
    min_colors = get_chromatic_number(states, neighbors)

    working_states = copy.deepcopy(states)
    colors = initialize_colors(states)
    domain = initialize_domain(states, min_colors)
    backtracks = 0

    if not use_heuristics:
        random.shuffle(working_states)

    # Run selected method
    if algorithm == 1:
        result = backtrack(working_states, neighbors, colors, domain, use_heuristics)
    elif algorithm == 2:
        result = forward_check(working_states, neighbors, colors, domain, use_heuristics)
    else:
        result = forward_check_with_singleton(working_states, neighbors, colors, domain, use_heuristics)

    time_elapsed = (datetime.now() - start_time).total_seconds() * 1000

    if result == "Success":
        print_solution(colors, min_colors, time_elapsed)
    else:
        print("\nNo Solution Found")
        print(f"Number of Backtracks: {backtracks}")
        print(f"Time Required to Compute: {time_elapsed:.2f} ms")


if __name__ == "__main__":
    main()
