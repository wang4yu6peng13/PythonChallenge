import re

findnothing = re.compile(r'Next nothing is (\d+)').match
seed ='90052'
while True:
    fname = 'channel/' + seed + '.txt'
    text = open(fname, 'r').read()
    m = findnothing(text)
    if m:
        seed = m.group(1)
    else:
        print(text)
        break