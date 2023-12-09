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
    print(cycle_ends)
    cycles.append((prefix, prefix_ends, cycle, cycle_ends))

# do something
