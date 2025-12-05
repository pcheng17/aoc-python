from common.utils import merge_intervals

def parse_data(input):
    data = input.split('\n\n')
    range_data = data[0].splitlines()
    ingredient_data = data[1].splitlines()
    ranges = []
    ingredients = []
    for r in range_data:
        ranges.append(list(map(int, r.split('-'))))
    for ing in ingredient_data:
        ingredients.append(int(ing))
    return ranges, ingredients

def part_a(input):
    ranges, ingredients = parse_data(input)
    ans = 0
    for ing in ingredients:
        for r in ranges:
            if r[0] <= ing <= r[1]:
                ans += 1
                break
    return ans

def part_b(input):
    ranges, _ = parse_data(input)
    ans = 0
    for x in merge_intervals(ranges):
        ans += x[1] - x[0] + 1
    return ans


