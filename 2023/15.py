def hash(v, c):
    v += ord(c)
    v *= 17
    v %= 256
    return v

def part_a(input):
    total = 0
    for word in input.split(','):
        value = 0
        for c in word:
            value = hash(value, c)
        total += value
    return total

def part_b(input):
    boxes = [[] for _ in range(256)]
    for word in input.split(','):
        h = 0
        for c in word:
            if c.isalpha():
                h = hash(h, c)
            else:
                break
        if '=' in word:
            key = word.split('=')[0]
            value = int(word.split('=')[1])
            if all(x[0] != key for x in boxes[h]):
                boxes[h].append((key, value))
            else:
                for i, (k, v) in enumerate(boxes[h]):
                    if k == key:
                        boxes[h][i] = (key, value)
                        break
        else:
            key = word.split('-')[0]
            for i, (k, v) in enumerate(boxes[h]):
                if k == key:
                    boxes[h].pop(i)
                    break
    
    total = 0
    for i, box in enumerate(boxes, 1):
        for j, lense in enumerate(box, 1):
            total += (i * j * lense[1])
    return total
            
            
            

