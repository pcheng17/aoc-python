def num_unique_vowels(string):
    vowels = 'aeiou'
    return sum(string.count(c) for c in vowels)

def has_double_letter(string):
    for i in range(0, len(string)-1):
        if string[i] == string[i+1]:
            return True
    return False

def contains_bad_substring(string):
    bad_substrs = ['ab', 'cd', 'pq', 'xy']
    return any(x in string for x in bad_substrs)

def has_double_pair(string):
    for i in range(0, len(string)-1):
        if string.count(string[i:i+2]) > 1:
            return True
    return False

def has_sandwich(string):
    for i in range(0, len(string)-2):
        if string[i] == string[i+2]:
            return True
    return False

def is_nice_a(string):
    return num_unique_vowels(string) >= 3 and has_double_letter(string) and not contains_bad_substring(string)

def is_nice_b(string):
    return has_double_pair(string) and has_sandwich(string)
    
def part_a(input):
    return sum(is_nice_a(line) for line in input.splitlines())

def part_b(input):
    return sum(is_nice_b(line) for line in input.splitlines())
