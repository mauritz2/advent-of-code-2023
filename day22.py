from functools import cmp_to_key

with open("inputs/22.txt") as f:
    def get_xyz(input):
        return list(map(int, input.split(",")))
        
    data = f.readlines()
    box_locs = []
    for row in data:
        start, end =  row.strip().split("~")
        box_locs.append((get_xyz(start), get_xyz(end)))

#def sort_by_lowest_z(block1, block2):
#    block1_min = min(block1[0][2], block1[1][2])
#    block2_min = min(block2[0][2], block2[1][2])
#    if block1_min < block2_min:
#        return -1
#    else:
#        return 1

#def is_overlap(range1, range2):
#    return (range1.start < range2.stop) and (range1.stop > range2.start)

#def can_fall(box_locs, box_loc):
#    if box_loc[2] == 1:
#        return False
#    x_hits = range(box_loc([0][0]), box_loc([0][0]))

def fall_one_step():



def fall_one_step()
    for box_i, box in enumerate(box_locs):
        box_minus_1_z = fall_one_step(box)

        # Check if it collides with anything

 
def is_colliding(rect1, rect2):
    for axis in [0, 1, 2]:
        if max(rect1[axis]) < min(rect2[axis]) or min(rect1[axis]) > max(rect2[axis]):
            return False
    return True



sorted_boxes = sorted(box_locs, key=cmp_to_key(sort_by_lowest_z))
# make them fall to the ground somehow
# check who is supporting which box

# Sort all pieces by lowest z-index

# while falling:
    # is z == 1:
        # Then stop
    # Does it hit anything in the x dimension? Does it hit anything in the y dimension?
        # Does my range overlap with any other boxes range (?) that's at or below this z index
        # if so - stop
    
    # Subtract the z dimension by one

# Settles positions
# Delete a block and simulate a fall
# Did anything change? No - then you can delete it 
