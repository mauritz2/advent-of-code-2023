from itertools import combinations

def expand_rows(universe:list[list[str]]) -> list[list[str]]:
    expanded_universe = []
    width = len(universe[0])

    for row_data in universe:
        if len([char for char in row_data if char != "."]) == 0:
            expanded_universe.append("." * width)
        expanded_universe.append(row_data)

    return expanded_universe

def expand_cols(universe:list[list[str]]) -> list[list[str]]:
    width = len(universe[0])

    # Transpose the matrix to work with rows instead of columns
    #transposed_universe = list(map(list, zip(*universe)))

    #expanded_universe_t = expand_rows(transposed_universe)


    col_nums_to_expand = []
    for col_num in range(width):
        if all([row[col_num] == "." for row in universe]):
            col_nums_to_expand.append(col_num)

    col_nums_to_expand.reverse()

    for col_num in col_nums_to_expand:
        for i, row in enumerate(universe):
            universe[i] = row[:col_num] + "X" + row[col_num:]
    return universe

def find_all_galaxies(universe: list[list[str]]) -> dict[int, tuple[int]]:
    galaxy_locs = {}
    galaxy_num = 1
    for y, row_data in enumerate(universe):
        last_x = 0
        while row_data.find("#", last_x) != -1:
            x = row_data.find("#", last_x)
            last_x = x + 1
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

def get_differences(galaxy_pairs, galaxies):
    differences = 0
    for g_1, g_2 in galaxy_pairs:
        g_1_loc = galaxies[g_1]
        g_2_loc = galaxies[g_2]

        y_diff = abs(g_1_loc[0] - g_2_loc[0])
        x_diff = abs(g_1_loc[1] - g_2_loc[1])
        total_diff = x_diff + y_diff
        print(f"For ({(g_1, g_2)} the difference is {total_diff}")
        differences += total_diff
    return differences

def main():
    universe = get_universe()
    for row in universe:
        print(row)
    galaxies = find_all_galaxies(universe)
    galaxy_pairs = list(combinations(galaxies, 2))
    print(get_differences(galaxy_pairs, galaxies))
    print(galaxies)


main()
