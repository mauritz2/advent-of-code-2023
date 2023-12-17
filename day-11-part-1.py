from itertools import combinations

def expand_rows(universe:list[list[str]]) -> list[list[str]]:
    row_to_expand = [i for i, col in enumerate(universe) if all(cell == "." for cell in col)]
    row_to_expand.reverse()
    for row_num in row_to_expand:
        universe.insert(row_num, "." * len(universe[0]))
    return universe

def expand_cols(universe:list[list[str]]) -> list[list[str]]:
    universe_t = ["".join(row) for row in zip(*universe)]
    expanded_universe_t = expand_rows(universe_t)
    expanded_universe = ["".join(row) for row in zip(*expanded_universe_t)]
    return expanded_universe

def find_all_galaxies(universe: list[list[str]]) -> dict[int, tuple[int]]:
    galaxy_locs = {}
    galaxy_num = 1
    for y, row_data in enumerate(universe):
        next_x_search_start = 0
        while row_data.find("#", next_x_search_start) != -1:
            x = row_data.find("#", next_x_search_start)
            next_x_search_start = x + 1
            galaxy_locs[galaxy_num] = (y, x)
            galaxy_num += 1
    return galaxy_locs

def get_universe():
    with open("day-11-data.txt") as f:
        data = f.readlines()
        data = [row.strip() for row in data]
        data = expand_rows(data)
        data = expand_cols(data)
    return data

def get_shortest_distance(galaxy_pairs, galaxies):
    differences = 0
    for g_1, g_2 in galaxy_pairs:
        g_1_loc = galaxies[g_1]
        g_2_loc = galaxies[g_2]
        y_diff = abs(g_1_loc[0] - g_2_loc[0])
        x_diff = abs(g_1_loc[1] - g_2_loc[1])
        total_diff = x_diff + y_diff
        differences += total_diff
    return differences

def main():
    universe = get_universe()
    galaxies = find_all_galaxies(universe)
    galaxy_pairs = list(combinations(galaxies, 2))
    print(get_shortest_distance(galaxy_pairs, galaxies))
    print(galaxies)

main()