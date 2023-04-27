# stack - last in first out ex: can of pringles
#search list
#[12,3,9,59,5,19].index(4)

#index into a  list

[3,6,9,12][3]

#copy list
[1,3,9][:]

#stack - last in first out
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
#implement stack  we .pop() last element
stack.pop()


queues = []
queues.append(1)
queues.append(2)
queues.append(3)

#removes first
queues.pop(1)


queues2 = []
queues2.insert(0, 1)
queues2.insert(0, 2)
queues2.insert(0, 3)

#remove first
queues2.pop(0)


opposite_directions = {
    'NORTH': 'SOUTH',
    'SOUTH': 'NORTH',
    'EAST': 'WEST',
    'WEST': 'EAST'
}
def reduce_directions(opposite_directions):
    new_direction = []
    for direction in opposite_directions:
        if new_direction and new_direction[-1] == opposite_directions[direction]:
            new_direction.pop()
        else:
            new_direction.append(direction)
    return new_direction
reduce_directions(opposite_directions)
