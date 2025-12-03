from collections import defaultdict

def part_a(input):
    data = input.splitlines()
    ans = 0
    for line in data:
        current_max = 0
        for i in range(len(line) - 1):
            for j in range(i + 1, len(line)):
                num = int(line[i]) * 10 + int(line[j])
                if num > current_max:
                    current_max = num
        ans += current_max
    return ans


def find_largest(num_str: str, digits: int) -> int:
    result = []
    start = 0

    for i in range(digits):
        remaining_needed = digits - i - 1
        search_end = len(num_str) - remaining_needed

        max_digit = num_str[start]
        max_pos = start

        for j in range(start, search_end):
            if num_str[j] > max_digit:
                max_digit = num_str[j]
                max_pos = j

        result.append(max_digit)
        start = max_pos + 1

    return int(''.join(result))

def part_b(input):
    data = input.splitlines()
    ans = 0
    for line in data:
        print(f"Line: ", line)
        x = find_largest(line, 12)
        print(f"Largest: ", x)
        ans += int(x)
    return ans
