def part_a(input):
    blocks = []
    for i, c in enumerate(input):
        fid = i // 2
        if i % 2 == 0:
            for j in range(int(c)):
                blocks.append(fid)
        else:
            for j in range(int(c)):
                blocks.append(-1)

    i = 0
    j = len(blocks)-1
    while blocks[j] == -1:
        j -= 1

    while i < j:
        if blocks[i] == -1 and blocks[j] != -1:
            blocks[i], blocks[j] = blocks[j], blocks[i]
            i += 1
            j -= 1
        else:
            if blocks[i] != -1:
                i += 1
            if blocks[j] == -1:
                j -= 1

    total = 0
    for i, x in enumerate(blocks):
        if x != -1:
            total += i * x

    return total

def part_b(input):
    filemap = {}
    holemap = {}
    block_count = 0
    for i, c in enumerate(input):
        fid = i // 2
        if i % 2 == 0:
            filemap[fid] = (block_count, int(c))
        else:
            holemap[block_count] = int(c)
        block_count += int(c)

    for fid in range(len(filemap)-1, -1, -1):
        block_count, block_size = filemap[fid]

        # Find the left-most hole that can fit the block_size
        smallest_hole_pos = block_count # Guaranteed to be larger than any hole
        for hole_pos, hole_size in holemap.items():
            if hole_size >= block_size and hole_pos < smallest_hole_pos:
                smallest_hole_pos = hole_pos

        if smallest_hole_pos == block_count:
            # Couldn't find a hole, move on
            continue

        filemap[fid] = (smallest_hole_pos, block_size)
        hole_size = holemap[smallest_hole_pos]

        del holemap[smallest_hole_pos]
        holemap[smallest_hole_pos + block_size] = hole_size - block_size

    total = 0
    for k, (begin, length) in filemap.items():
        for i in range(begin, begin+length):
            total += (i * k)

    return total



