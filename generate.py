import sys

segments = int(sys.argv[1])

boy = ""

with open("svgs/base.svg") as f:
    base = f.read()

with open("svgs/up.svg") as f: 
    up = f.read()

with open("svgs/down.svg") as f: 
    down = f.read()

with open("svgs/tail.svg") as f:
    tail = f.read()

PLACE = 110
COLOUR_PLACE = 0
COLOURS = ["00b25a","ffc519","f3703a","e11d43","5b57a6"]

UP_OFFSET = 0 
DOWN_OFFSET = 62 

def colour(offset=0):
    global COLOUR_PLACE
    COLOUR_PLACE += 1
    return COLOURS[(COLOUR_PLACE + offset) % len(COLOURS)]

def upboy(offset=0): 
    global PLACE
    PLACE += DOWN_OFFSET
    return up.format(PLACE + offset, colour())

def downboy(offset=0): 
    global PLACE
    PLACE += UP_OFFSET
    return down.format(PLACE + 8, colour())

boy = ""
for s in range(0,segments):
    boy += upboy() + downboy()

length = PLACE + 200
boy = base.format(length) + boy

boy += tail.format(PLACE + 38, colour(-1))

with open("generated_%s.svg" % segments, "w") as f:
    f.write(boy)
