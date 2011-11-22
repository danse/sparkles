import sys

def echo(line):
    return line

for line in sys.stdin:
    line = echo(line)
    if line:
        sys.stdout.write(line)
