from pathlib import Path

puzzle_input = (Path(__file__).parents[1] / "data" / "day01.txt").read_text()
puzzle_input = puzzle_input.splitlines()
puzzle_input = [int(n) for n in puzzle_input]
#print(puzzle_input)


def fuel_requirement(mass: int) -> int:
    return (mass // 3) - 2

assert fuel_requirement(12) == 2
assert fuel_requirement(14) == 2
assert fuel_requirement(1969) == 654
assert fuel_requirement(100756) == 33583

fuel_required = 0
for mass in puzzle_input:
    fuel_required += fuel_requirement (mass)
print(f" part 1 {fuel_required}")

total_fuel_required = 0
for mass in puzzle_input:
    fuel_required = 0
    # to lift the module
    fuel_required += (fuel_add:=fuel_requirement (mass))

    # fuel to lift the fuel
    while (fuel_add:=fuel_requirement(fuel_add)) > 0:
        fuel_required += fuel_add
    total_fuel_required += fuel_required

print(f" part 2 {total_fuel_required}")
