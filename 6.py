"""
Solution using the inequality boundary algorithm

In a race t seconds long we spend x miliseconds charging then go x milimeters
per milisecond for the remaining x - t miliseconds, and we must end up going
further than n miliseconds in total. So, x * (t - x) > n. This is a quadratic
inequality that we need to solve.

x * (t - x) > n
xt - x**2 > n
-xt + x**2 < -n
x**2 - tx - n < 0

BOUNDRY POINTS:
    discrim = (t**2 + 4*n)**0.5
    x = (discrim + t) / 2
    x = (-discrim + t) / 2

Find the integers strictly between and not including the boundary points, as
at the boundary points x * (t - x) = n, but we need to be greater than n.
"""

with open('6.txt') as f:
    times = [int(x) for x in f.readline()[5:].strip().split(' ') if x != '']
    dists = [int(x) for x in f.readline()[9:].strip().split(' ') if x != '']

# part 1

prod = 1
for i in range(len(times)):
    t = times[i]
    n = dists[i]
    discrim = (t**2 - 4*n)**0.5
    bp1 = (discrim + t) / 2
    bp2 = (-discrim + t) / 2
    bp1 -= 1 if bp1 % 1 == 0 else bp1 % 1
    bp2 += 1 if bp2 % 1 == 0 else 1 - bp2 % 1
    prod *= bp1 - bp2 + 1
print(prod)

# part 2
# the previous solution is really fast, so just do it again

with open('6.txt') as f:
    t = int(f.readline()[5:].strip().replace(' ', ''))
    n = int(f.readline()[9:].strip().replace(' ', ''))

discrim = (t**2 - 4*n)**0.5
bp1 = (discrim + t) / 2
bp2 = (-discrim + t) / 2
bp1 -= 1 if bp1 % 1 == 0 else bp1 % 1
bp2 += 1 if bp2 % 1 == 0 else 1 - bp2 % 1
print(bp1 - bp2 + 1)
