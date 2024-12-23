import itertools

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
        print(f"A={self.a}, B={self.b}, C={self.c}, Output={self.output}")
        while i < len(self.program):
            result = self.ops[self.program[i]](self.program[i + 1])
            if result is None:
                i += 2
            else:
                i = result

            print(f"A={self.a}, B={self.b}, C={self.c}, Output={self.output}")

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
    # return ','.join(map(str, machine.output))

def part_b(input):
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
