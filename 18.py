from collections import deque

# part 1

# parse
g = {}
x = 0
y = 0
for line in open('18.txt'):
    dr, num, color = line.strip().split(' ')
    num = int(num)
    color = color[2:-1]
    for i in range(num):
        g[(x, y)] = color
        if dr == 'R':
            x += 1
        elif dr == 'L':
            x -= 1
        elif dr == 'U':
            y -= 1
        elif dr == 'D':
            y += 1

# flood fill
q = deque([(1, 1)])
visited = set([(1, 1)])
while q:
    v = q.pop()
    visited.add(v)
    edges = [(v[0] - 1, v[1]), (v[0] + 1, v[1]), (v[0], v[1] - 1),
             (v[0], v[1] + 1)]
    for e in edges:
        if e in visited or e in g:
            continue
        q.append(e)

print(len(g) + len(visited))

# part 2

# reparse the input
verts = [(0, 0)]
perim = 0
drs = []
for line in open('18.txt'):
    color = line.split(' ')[2]
    dist = int(color[2:-3], 16)
    perim += dist
    dr = int(color[-3])
    if dr == 0:
        verts.append((verts[-1][0] + dist, verts[-1][1]))
    elif dr == 1:
        verts.append((verts[-1][0], verts[-1][1] - dist))
    elif dr == 2:
        verts.append((verts[-1][0] - dist, verts[-1][1]))
    elif dr == 3:
        verts.append((verts[-1][0], verts[-1][1] + dist))
    drs.append(dr)
verts = verts[1:]

# order matters
if drs[0] == 0 or drs[0] == 3:
    verts.reverse()

# shoelace formula
area = 0
for i in range(len(verts) - 1):
    area += verts[i][0]*verts[i+1][1] - verts[i][1]*verts[i+1][0]
area += verts[-1][0]*verts[0][1] - verts[0][0]*verts[-1][1]
area /= 2 if area > 0 else -2

# picks theorem
# A = i + b/2 - 1
# A - b/2 + 1 = i
inside = area - perim/2 + 1
print(inside + perim)
