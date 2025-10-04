import sys
from collections import defaultdict

class Kernel:
    def __init__(self,indexes,rules):
        self.idxs = indexes
        self.rules = rules

    def update(self,alive):
        neighbors = defaultdict(int)
        for p in alive:
            for idx in self.idxs:
                n = idx(p)
                neighbors[n] += 1
        next_gen = set()
        for n in neighbors:
            if neighbors[n] in self.rules[1 if n in alive else 0]:
                next_gen.add(n)
        return next_gen

    def get(self,board,p):
        s = 0
        for idx in self.idxs:
            i,j = idx(p)
            s += board[i][j]
        if s in self.rules[board[p[0]][p[1]]]:
            return 1
        else:
            return 0

    @classmethod
    def parse(cls,path):
        with open(path,'r') as f:
            h,w = tuple([int(n) for n in f.readline().split()])
            f.readline()
            grid = []
            ci,cj = None, None
            for i in range(h):
                grid.append([])
                line = f.readline()
                for j in range(w):
                    if line[j] == 'c':
                        ci,cj = i,j
                        grid[-1].append(1)
                    else:
                        grid[-1].append(int(line[j]))
            indexes = set()
            for i in range(h):
                for j in range(w):
                    if grid[i][j]:
                        indexes.add(lambda t, ii=i, jj=j: (ci-ii+t[0],cj-jj+t[1]))
            rules = defaultdict(set)
            f.readline()
            while l := f.readline():
                s,n = l.split(':')
                rules[int(s)].add(int(n))
            return Kernel(indexes,rules)

def main():
    k = Kernel.parse(sys.argv[1])

if __name__ == '__main__':
    main()
