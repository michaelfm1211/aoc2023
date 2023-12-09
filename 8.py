from math import gcd

# part 1

lines = [line.strip() for line in open("8.txt")]
dirs = [0 if ch == "L" else 1 for ch in lines[0]]
g = {}
for line in lines[2:]:
    parts = line.split(" ")
    g[parts[0]] = (parts[2][1:-1], parts[3][:-1])

# probably a more elegant way than this bute force way, but it works
steps = 0
curr = 'AAA'
while curr != 'ZZZ':
    curr = g[curr][dirs[steps % len(dirs)]]
    steps += 1
print(steps)

# part 2

"""
This is kind of a cheat based on the input. First, we follow each starting
point until we get to a cycle, then use that cycle to figure out when all the
end point indicies will align.

This assumes that the endpoints don't occur before any of the paths reach
a cycle and that there is only one endpoint per cycle, which just happens to be
true. From there, we can consider the cycles and the end nodes to form a
system of linear congruences. I don't write code to solve that system though,
so I'll just spit it out and have the user figure it out for themselves.
Cheating? Probably.

This problem can actually be solved even faster if also take the assumption
that it takes n steps to get from the start to the end node, and that the
length of the cycle is also n. This happens to be true for the input, but that
feels a bit too much like cheatng.
"""

# find cycles
starts = [node for node in g if node[-1] == 'A']
cycles = []
for start in starts:
    path = [start]
    step = 0
    ind = -1
    while True:
        next_node = g[path[-1]][dirs[step % len(dirs)]]
        if next_node in path and step % len(dirs) == (
                path.index(next_node) - 1) % len(dirs):
            ind = path.index(next_node)
            break
        path.append(next_node)
        step += 1

    prefix = path[:ind]
    prefix_ends = [i for i, node in enumerate(prefix) if node[-1] == 'Z']
    cycle = path[ind:]
    cycle_ends = [i for i, node in enumerate(cycle) if node[-1] == 'Z']
    cycles.append((len(prefix), prefix_ends, len(cycle), cycle_ends))

# fast forward the length of the longest prefix to get to the cycle
ff_len = max(cycle[0] for cycle in cycles)
ff_cycles = []
for cycle in cycles:
    offset = ff_len - cycle[0]
    ff_cycles.append((cycle[2], [ind - offset for ind in cycle[3]]))

# solve a system of linear congruences
print('Solve this system of linear congruences:')
for cyc in ff_cycles:
    print(f'\tn = {cyc[1][0]} (mod {cyc[0]})')
print(f'then add {ff_len - 1}')

# add the ff_len- 1 to the answer, as that's how much we originally went
# forward and subtract 1 because we originally includes the start node.
