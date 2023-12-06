keys = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
    # 'cid'
]

def parse(raw_data):
    raw_data_as_list = raw_data.split('\n\n')
    data = [] 
    for element in raw_data_as_list:
        params = element.split()
        d = {}
        for p in params:
            key, value = p.split(':')
            d[key] = value
        data.append(d)
    return data

def split_number_and_units(string):
    number = ''
    unit = ''
    for c in string:
        if c.isdigit():
            number += c
        else:
            unit += c
    return int(number), unit

def in_range(value, min, max):
    return min <= value and value <= max

def check_present(passport):
    return all([k in passport for k in keys])

def check_valid(passport):
    if not in_range(int(passport['byr']), 1920, 2002):
        return False
    
    if not in_range(int(passport['iyr']), 2010, 2020):
        return False

    if not in_range(int(passport['eyr']), 2020, 2030):
        return False

    hgt, unit = split_number_and_units(passport['hgt'])
    if unit == 'cm':
        if not in_range(hgt, 150, 193):
            return False
    elif unit == 'in':
        if not in_range(hgt, 59, 76):
            return False
    else:
        return False
    
    hcl = passport['hcl']
    if hcl[0] != '#':
        return False
    else:
        if len(hcl) != 7:
            return False
    
    valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if passport['ecl'] not in valid_ecl:
        return False

    if len(passport['pid']) != 9:
        return False
    
    return True

def part_a(input):
    valid = 0
    for passport in parse(input):
        if check_present(passport):
            valid += 1
    return valid

def part_b(input):
    valid = 0
    for passport in parse(input):
        if check_present(passport) and check_valid(passport):
            valid += 1
    return valid
