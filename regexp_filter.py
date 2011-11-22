import sys
import re

examples=(
    # python /tmp/r.py '      2 \$mam_user     = (.+);'
    ('      2 $mam_user     = 102546;', '      2 \$mam_user     = (.+);', '102546\n'),
    # ('', '', ''),
)

class Filter:
    '''
    >>> for example in examples:
    ...  f = Filter(example[1])
    ...  l = f.filter(example[0])
    ...  assert l == example[2], 'l: {0}, e: {1}'.format(l, example[2])
    '''

    def __init__(self, regexp):
        self.__regexp = regexp

    def filter(self, line):
        m = re.search(self.__regexp, line)
        if m:
            return m.group(1)+'\n'

f=Filter(sys.argv[1])
for line in sys.stdin:
    filtered = f.filter(line)
    if filtered:
        sys.stdout.write(filtered)
