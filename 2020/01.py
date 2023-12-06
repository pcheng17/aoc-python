def parse(input):
    return list(map(int, input.splitlines()))

def part_a(input):
    nums = parse(input)

    seen = set()

    for n in nums:
        x = 2020 - n
        if x in seen:
            return n * x
        seen.add(n)

def part_b(input):
    nums = sorted(parse(input))
    for i in range(len(nums)):
        j = i + 1
        k = len(nums) - 1
        while j < k:
            if nums[i] + nums[j] + nums[k] == 2020:
                return nums[i] * nums[j] * nums[k]
            elif nums[i] + nums[j] + nums[k] < 2020:
                j += 1
            else:
                k -= 1
