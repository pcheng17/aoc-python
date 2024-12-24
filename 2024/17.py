import sys
class Machine:
    def __init__(self, a, b, c, program):
        self.a = a
        self.b = b
        self.c = c
        self.program = program
        self.ops = (
            self.adv,
            self.bxl,
            self.bst,
            self.jnz,
            self.bxc,
            self.out,
            self.bdv,
            self.cdv
        )
        self.output = []

    def run(self):
        self.output = []
        i = 0
        while i < len(self.program):
            result = self.ops[self.program[i]](self.program[i + 1])
            if result is None:
                i += 2
            else:
                i = result

    def combo(self, n):
        if n < 0 or n > 7:
            raise ValueError(f"Invalid combo: {n=}")
        match n:
            case 4:
                return self.a
            case 5:
                return self.b
            case 6:
                return self.c
        return n

    def adv(self, operand):
        self.a >>= self.combo(operand)

    def bxl(self, operand):
        self.b ^= operand

    def bst(self, operand):
        self.b = self.combo(operand) % 8

    def jnz(self, operand):
        if self.a == 0:
            return
        return operand

    def bxc(self, operand):
        self.b ^= self.c

    def out(self, operand):
        self.output.append(self.combo(operand) % 8)

    def bdv(self, operand):
        self.b = self.a >> self.combo(operand)

    def cdv(self, operand):
        self.c = self.a >> self.combo(operand)

def part_a(input):
    registers, program = input.split('\n\n')
    A = B = C = 0
    rows = registers.splitlines()
    A = int(rows[0].split(': ')[1])
    B = int(rows[1].split(': ')[1])
    C = int(rows[2].split(': ')[1])
    program = list(map(int, program.split(': ')[1].split(',')))

    machine = Machine(A, B, C, program)
    machine.run()
    return ','.join(map(str, machine.output))

def part_b(input):
    registers, program = input.split('\n\n')
    A = B = C = 0
    rows = registers.splitlines()
    A = int(rows[0].split(': ')[1])
    B = int(rows[1].split(': ')[1])
    C = int(rows[2].split(': ')[1])
    program = list(map(int, program.split(': ')[1].split(',')))

    constraints = []
    for n in range(8):
        tmp = []
        for b in range(8):
            c1 = b ^ 2 ^ 3          # Bottom 3 bits
            m1 = 7                  # Mask of bottom 3 bits
            c2 = (b ^ n) << (b ^ 3) # Other 3 bits
            m2 = 7 << (b ^ 3)       # Mask of other 3 bits
            m = m1 & m2             # Intersection of masks
            if c1 & m == c2 & m:
                tmp.append((c1 | c2, m1 | m2)) # Merge the two numbers
        constraints.append(tmp)

    candidates = set(constraints[program[0]])
    for i in range(len(program)):
        goal = program[i]
        z = set((c << (3 * i), m << (3 * i)) for c, m in constraints[goal])
        new_candidates = set()

        for (constraint, mask_constraint) in z:
            for (candidate, mask_candidate) in candidates:
                m = mask_candidate & mask_constraint
                if (candidate & m) == (constraint & m):
                    new_candidates.add((candidate | constraint, mask_candidate | mask_constraint))

        candidates = new_candidates

    A = min(candidates, key=lambda x: x[0])[0]
    machine = Machine(A, B, C, program)
    machine.run()

    return min(candidates, key=lambda x: x[0])[0]
