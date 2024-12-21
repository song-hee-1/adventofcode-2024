part1_directions = [(0, -1), (0, 1), (-1, 0), (1, 0),
              (-1, -1), (-1, 1), (1, -1), (1, 1)]

def count_xmas(grid: list[str]):
    rows, cols = len(grid), len(grid[0])
    target = "XMAS"
    target_len = len(target)
    count = 0

    def is_valid(x, y):
        return 0 <= x < cols and 0 <= y < rows

    for y in range(rows):
        for x in range(cols):
            if grid[y][x] == 'X':
                for dx, dy in part1_directions:
                    found = True
                    for i in range(target_len):
                        nx, ny = x + dx * i, y + dy * i
                        if not is_valid(nx, ny) or grid[ny][nx] != target[i]:
                            found = False
                            break
                    if found:
                        count += 1
    return count


left_diagonal = [(-1, -1), (1, 1)]
right_diagonal = [(1, -1), (-1, 1)]
def count_mas(grid: list[str]):
    rows, cols = len(grid), len(grid[0])
    target = "MS"
    target_reversed = "SM"
    count = 0
    def is_valid(x, y):
        return 0 <= x < cols and 0 <= y < rows
    for y in range(rows):
        for x in range(cols):
            if grid[y][x] == 'A':
                left_diag = ""
                left_flag = True
                for dx, dy in left_diagonal:
                    nx, ny = x + dx, y + dy
                    if is_valid(nx, ny):
                        left_diag += grid[ny][nx]
                    else:
                        left_flag = False
                        break

                right_diag = ""
                right_flag = True
                for dx, dy in right_diagonal:
                    nx, ny = x + dx, y + dy
                    if is_valid(nx, ny):
                        right_diag += grid[ny][nx]
                    else:
                        right_flag = False
                        break
                if left_flag and right_flag and left_diag in (target, target_reversed) and right_diag in (
                target, target_reversed):
                    count += 1
    return count


with open("day4/part1_input.txt", "r") as file:
    part1_grid = [line.strip() for line in file]

result = count_xmas(part1_grid)
print(f"part 1의 답 : XMAS appears {result} times.")

with open("day4/part2_input.txt", "r") as file:
    part2_grid = [line.strip() for line in file]

result = count_mas(part2_grid)
print(f"part 2의 답 : MAS appears {result} times.")






