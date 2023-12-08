from common.utils import crt
from operator import mul
from functools import reduce


def parse(raw_data):
    split_data = raw_data.splitlines()
    timestamp = int(split_data[0])
    bus_ids_list = split_data[1].split(',')
    return timestamp, bus_ids_list

def part_a(input):
    timestamp, bus_ids_list = parse(input)
    bus_ids = set([int(x) for x in bus_ids_list if x.isnumeric()])
    for t in range(timestamp, timestamp + max(bus_ids) + 1):
        for id in bus_ids:
            if t % id == 0:
                return (t - timestamp) * id

def part_b(input):
    _, bus_ids_list = parse(input)
    crt_data = [(i, int(x)) for i, x in enumerate(bus_ids_list) if x.isnumeric()]
    crt_data_zero = [(-a % b, b) for a, b in crt_data]

    # This array now phrases the question as follows:
    # Find the smallest t such that:
    # for (a, n) in crt_data_zero:
    #     t ≡ a (mod n)

    return crt(crt_data_zero)
    
