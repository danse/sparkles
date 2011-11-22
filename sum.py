import sys

class Sum:

    def __init__(self):
        self.__total = 0.0

    def add(self, line):
        # Ignore lines which can not be converted
        try:
            f = float(line)
        except:
            try:
                f = float(line.split()[0])
            except:
                return
        self.__total += f

    @property
    def total(self):
        if self.__total.is_integer():
            t = int(self.__total)
        return str(t)+'\n'

s=Sum()
for line in sys.stdin:
    s.add(line)
sys.stdout.write(s.total)
