def parse_input(file_path):
    """입력 데이터를 읽어 각 줄을 정수 리스트로 변환."""
    with open(file_path, "r") as f:
        return [list(map(int, line.strip().split())) for line in f.readlines()]


def check_trend_and_safety(current, next_element, is_increased, is_decreased):
    """
    두 요소 간의 차이를 계산하고 경향성을 확인.
    - 차이가 1~3 사이인지 검증.
    - 증가, 감소 여부를 플래그로 갱신.
    """
    diff = next_element - current
    if not (1 <= abs(diff) <= 3):
        return False, is_increased, is_decreased

    if diff > 0:
        is_increased = True
    elif diff < 0:
        is_decreased = True

    # 증가와 감소가 동시에 발생하면 안전하지 않음
    if is_increased and is_decreased:
        return False, is_increased, is_decreased

    return True, is_increased, is_decreased


def is_list_safe(element_list):
    """주어진 리스트가 안전한지 확인."""
    is_increased, is_decreased = False, False
    for i in range(len(element_list) - 1):
        is_safety, is_increased, is_decreased = check_trend_and_safety(
            element_list[i], element_list[i + 1], is_increased, is_decreased
        )
        if not is_safety:
            return False
    return True


def count_safe_reports_with_dampener(lines):
    """
    각 줄을 검사하여 조건에 맞는 보고서 개수를 반환.
    - 기본적으로 안전한 보고서 카운트.
    - 하나의 숫자를 제거해서 안전해질 수 있는 경우도 포함.
    """
    safety_report_count = 0

    for element_list in lines:
        # 원본 리스트가 안전한 경우
        if is_list_safe(element_list):
            safety_report_count += 1
            continue

        # 하나씩 제거하면서 검사
        for i in range(len(element_list)):
            modified_list = element_list[:i] + element_list[i + 1:]
            if is_list_safe(modified_list):
                safety_report_count += 1
                break

    return safety_report_count


file_path = "day2/input.txt"
lines = parse_input(file_path)

# Part 1: 안정성 보고서
part_1_count = sum(is_list_safe(line) for line in lines)
print(f"안정성 보고서 (파트 1): {part_1_count}개")

# Part 2: The Problem Dampener 적용 안정성 보고서
part_2_count = count_safe_reports_with_dampener(lines)
print(f"The Problem Dampener 적용 안정성 보고서 (파트 2): {part_2_count}개")
