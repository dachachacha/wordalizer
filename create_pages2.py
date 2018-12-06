import sys
import collections
from random import shuffle, SystemRandom
sysrand = SystemRandom().random

sys.setrecursionlimit(7000)

words_per_line = 15
char_per_line = 55
lines_per_page = 35

def create_lines(bag, nlines = lines_per_page):
    lines = []
    words = []
    char_cnt = 0
    while char_cnt < char_per_line and bag:
        new = bag.pop()
        words.append(new)
        char_cnt += len(new)
    lines.append(" ".join(words))
    nlines -= 1
    if nlines ==  0: 
        lines += [""]
        nlines = lines_per_page
    if bag:
        return lines + create_lines(bag, nlines)
    else: return lines

def create_text(bag):
    shuffle(bag, sysrand)
    return bag

def get_title(bag, numw = 3):
    if numw > 0:
        r = SystemRandom().randint(0,len(bag))
        w = [bag[r]]
        return w + get_title(bag,numw - 1)
    else: return []

import json
with open('wordcount.json',encoding='utf-8') as fp:
    bag = collections.Counter(json.load(fp))
flat_bag = list(bag.elements())

title = " ".join(get_title(flat_bag))
words = create_text(flat_bag)
lines = create_lines(words)
text = "\n".join(lines)

with open('text.txt','w',encoding='utf-8') as fp:
    fp.write(title + "\n\n" + text)
