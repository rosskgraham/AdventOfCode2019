from itertools import pairwise

# Don't need to check if length == 6, puzzle range is between two 6 digit numbers.


def has_two_adjacent_same(num: int) -> bool:
    digits = [int(n) for n in str(num)]
    return any(a == b for a, b in pairwise(digits))


def has_two_adjacent_same_not_part_of_larger_group(num: int) -> bool:
    digits = [int(n) for n in str(num)]
    groups = [[digits[0]]]
    for digit in digits[1:]:
        if digit == groups[-1][-1]:
            groups[-1].append(digit)
        else:
            groups.append([digit])
    return any(len(g) == 2 for g in groups)


def digits_never_decrease(num: int) -> bool:
    digits = [int(n) for n in str(num)]
    return all(a <= b for a, b in pairwise(digits))


part1_passwords, part2_passwords = 0, 0
for num in range(153517, 630395 + 1):
    if has_two_adjacent_same(num) and digits_never_decrease(num):
        part1_passwords += 1
    if has_two_adjacent_same_not_part_of_larger_group(num) and digits_never_decrease(
        num
    ):
        part2_passwords += 1

print(f"1. {part1_passwords} passwords")
print(f"2. {part2_passwords} passwords")
