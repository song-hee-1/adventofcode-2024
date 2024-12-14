def read_input(file_path: str):
    """파일에서 데이터를 읽어와 왼쪽 및 오른쪽 요소 리스트를 정렬하여 반환합니다."""
    left_list, right_list = [], []

    with open(file_path, 'r') as f:
        for line in f:
            left_element, right_element = line.split('   ')
            left_list.append(int(left_element))
            right_list.append(int(right_element.strip('\n')))

    return sorted(left_list), sorted(right_list)


def calculate_difference(left_list, right_list):
    """왼쪽 리스트와 오른쪽 리스트 간의 총 차이를 계산합니다."""
    differ = sum(abs(right - left) for right, left in zip(left_list, right_list))
    return differ


def calculate_similarity(left_list, right_list):
    """리스트의 요소 발생 빈도를 기반으로 유사성을 계산합니다."""
    similarity = 0
    for left in left_list:
        count = right_list.count(left)
        similarity += (left * count)
    return similarity


# 메인 실행부
path = "day1/input.txt"
left_element_list, right_element_list = read_input(path)

# 파트 1: 차이 계산
difference = calculate_difference(left_element_list, right_element_list)
print(f"총 차이: {difference}")

# 파트 2: 유사성 계산
similarity_score = calculate_similarity(left_element_list, right_element_list)
print(f"유사성: {similarity_score}")
