import sys

def extract_cdr_field(line, field):
    pairs = line.split()
    for pair in pairs:
        try:
            l_field, l_value = pair.split('=')
            if l_field == field:
                return l_value.strip('"')+'\n'
        except:
            pass
    return None

for line in sys.stdin:
    line = extract_cdr_field(line, sys.argv[1])
    if line:
        sys.stdout.write(line)
