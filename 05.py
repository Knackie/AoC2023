
class Function:
    def __init__(self, s):
        lines = s.split('\n')[1:]  # throw away name
        self.tuples = [[int(x) for x in line.split()] for line in lines]

    def apply_one(self, x):
        for (dst, src, sz) in self.tuples:
            if src <= x < src + sz:
                return x + dst - src
        return x

    def apply_range(self, R):
        A = []
        for (dest, src, sz) in self.tuples:
            src_end = src + sz
            NR = []
            while R:
                (st, ed) = R.pop()
                before = (st, min(ed, src))
                inter = (max(st, src), min(src_end, ed))
                after = (max(src_end, st), ed)
                if before[1] > before[0]:
                    NR.append(before)
                if inter[1] > inter[0]:
                    A.append((inter[0] - src + dest, inter[1] - src + dest))
                if after[1] > after[0]:
                    NR.append(after)
            R = NR
        return A + R

def main():
    D = open(sys.argv[1]).read().strip()
    parts = D.split('\n\n')
    seed, *others = parts

    seed = [int(x) for x in seed.split(':')[1].split()]
    Fs = [Function(s) for s in others]

    P1 = [min([f.apply_one(x) for f in Fs]) for x in seed]
    print(min(P1))

    P2 = [min(f.apply_range([(st, st + sz) for st, sz in zip(seed[::2], seed[1::2])]))[0] for f in Fs]
    print(min(P2))

if __name__ == "__main__":
    main()
