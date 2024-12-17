import re


def process_part1(file_path):
    part1_answer = 0
    with open(file_path, 'r') as f:
        for line in f:
            matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', line)
            for x, y in matches:
                part1_answer += int(x) * int(y)
    return part1_answer


def process_part2(file_path):
    part2_answer = 0
    is_active = True
    pattern = r"(mul\((\d+),(\d+)\))|don't\(\)|do\(\)"

    with open(file_path, 'r') as f:
        for line in f:
            for match in re.finditer(pattern, line):
                if match.group(2) and match.group(3):  # mul(x, y)
                    if is_active:
                        part2_answer += int(match.group(2)) * int(match.group(3))
                elif "don't()" in match.group(0):  # disable
                    is_active = False
                elif "do()" in match.group(0):  # enable
                    is_active = True
    return part2_answer


part1_answer = process_part1("day3/part1_input.txt")
print(f"part 1의 답 : {part1_answer}")

part2_answer = process_part2("day3/part2_input.txt")
print(f"part 2의 답 : {part2_answer}")
