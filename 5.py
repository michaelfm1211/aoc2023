lines = [line.strip() for line in open('5.txt')]


def parse_map(lineno):
    maps = []
    while lineno < len(lines) and lines[lineno] != '':
        maps.append([int(num) for num in lines[lineno].split(' ')])
        lineno += 1
    return lineno, maps


# for part 1
def use_map(inps, maps):
    outputs = []
    for inp in inps:
        mapped = False
        for m in maps:
            if inp in range(m[1], m[1] + m[2]):
                outputs.append(inp - m[1] + m[0])
                mapped = True
        if not mapped:
            outputs.append(inp)
    return outputs


# for part 2
def use_map_with_range(rngs, maps):
    outputs = []
    for rng in rngs:
        mapped = False
        for m in maps:
            # we only want to map the intersection of the range and the map,
            # then punt off the rest of the range by cutting it up into new
            # ranges and considering them as inputs later.
            # if there is no intersection, continue, but if we find an
            # intersection and cut up the current range, then don't do extra
            # work by looking and more maps

            # find the intersection between the range and the map. if it exists
            # then add the mapped range to the output
            intsec_start = max(rng[0], m[1])
            intsec_end = min(rng[0] + rng[1], m[1] + m[2])
            intsec_len = intsec_end - intsec_start
            if intsec_len <= 0:
                continue
            mapped_range = (intsec_start - m[1] + m[0], intsec_len)
            outputs.append(mapped_range)
            mapped = True

            first_len = intsec_start - rng[0]
            if first_len > 0:
                rngs.append((rng[0], first_len))
            last_len = rng[0] + rng[1] - intsec_end - 1
            if last_len > 0:
                rngs.append((intsec_end, last_len))
            break
        if not mapped:
            outputs.append(rng)

    return outputs


lineno, seed_soil_map = parse_map(3)
lineno, soil_fert_map = parse_map(lineno + 2)
lineno, fert_water_map = parse_map(lineno + 2)
lineno, water_lights_map = parse_map(lineno + 2)
lineno, light_temp_map = parse_map(lineno + 2)
lineno, temps_humid_map = parse_map(lineno + 2)
lineno, humid_loc_map = parse_map(lineno + 2)

# part 1

seeds = [int(num) for num in lines[0].split(': ')[1].split(' ')]
soils = use_map(seeds, seed_soil_map)
ferts = use_map(soils, soil_fert_map)
waters = use_map(ferts, fert_water_map)
lights = use_map(waters, water_lights_map)
temps = use_map(lights, light_temp_map)
humids = use_map(temps, temps_humid_map)
locs = use_map(humids, humid_loc_map)
print(min(locs))

# part 2

nums = [int(num) for num in lines[0].split(': ')[1].split(' ')]
seeds = [(nums[i], nums[i + 1]) for i in range(0, len(nums), 2)]
soils = use_map_with_range(seeds, seed_soil_map)
ferts = use_map_with_range(soils, soil_fert_map)
waters = use_map_with_range(ferts, fert_water_map)
lights = use_map_with_range(waters, water_lights_map)
temps = use_map_with_range(lights, light_temp_map)
humids = use_map_with_range(temps, temps_humid_map)
locs = use_map_with_range(humids, humid_loc_map)
print(min(locs))
