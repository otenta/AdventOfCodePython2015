import re

#Actually had no idea it was this easy. I made a giant string for wire a and tried to evaluate it
#but couldn't get it to work. This is chat gpt. I admit defeat


TOKEN = r'(?:\d+|[a-z]+)'

PATTERN_ASSIGN = re.compile(rf'^({TOKEN})$')
PATTERN_NOT    = re.compile(rf'^NOT\s+({TOKEN})$')
PATTERN_AND    = re.compile(rf'^({TOKEN})\s+AND\s+({TOKEN})$')
PATTERN_OR     = re.compile(rf'^({TOKEN})\s+OR\s+({TOKEN})$')
PATTERN_LSHIFT = re.compile(rf'^({TOKEN})\s+LSHIFT\s+(\d+)$')
PATTERN_RSHIFT = re.compile(rf'^({TOKEN})\s+RSHIFT\s+(\d+)$')

rules = {}

with open("input.txt") as f:
    for line in f:
        if not line.strip():
            continue
        lhs, dst = map(str.strip, line.split("->"))
        if m := PATTERN_ASSIGN.match(lhs):
            (a,) = m.groups(); rules[dst] = ('ASSIGN', a)
        elif m := PATTERN_NOT.match(lhs):
            (a,) = m.groups(); rules[dst] = ('NOT', a)
        elif m := PATTERN_AND.match(lhs):
            a,b = m.groups(); rules[dst] = ('AND', a, b)
        elif m := PATTERN_OR.match(lhs):
            a,b = m.groups(); rules[dst] = ('OR', a, b)
        elif m := PATTERN_LSHIFT.match(lhs):
            a,n = m.groups(); rules[dst] = ('LSHIFT', a, int(n))
        elif m := PATTERN_RSHIFT.match(lhs):
            a,n = m.groups(); rules[dst] = ('RSHIFT', a, int(n))
        else:
            raise ValueError(f"Cannot parse: {line!r}")

from functools import lru_cache

@lru_cache(None)
def value(tok: str) -> int:
    return int(tok) if tok.isdigit() else eval_wire(tok)

@lru_cache(None)
def eval_wire(w: str) -> int:
    op = rules[w]
    kind = op[0]
    if kind == 'ASSIGN':
        res = value(op[1])
    elif kind == 'NOT':
        res = ~value(op[1])
    elif kind == 'AND':
        res = value(op[1]) & value(op[2])
    elif kind == 'OR':
        res = value(op[1]) | value(op[2])
    elif kind == 'LSHIFT':
        res = value(op[1]) << op[2]
    elif kind == 'RSHIFT':
        res = value(op[1]) >> op[2]
    else:
        raise RuntimeError("unknown op")
    return res & 0xFFFF

print(eval_wire("a"))
