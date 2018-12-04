import sys
from random import shuffle, SystemRandom

sys.setrecursionlimit(7000)

words_per_line = 15
char_per_line = 55
lines_per_page = 35
bag_of_words = open('words.txt',encoding='utf-8').read().split()
shuffle(bag_of_words, SystemRandom().random)

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
        lines += ["\n"]
        nlines = lines_per_page
    if bag:
        return lines + create_lines(bag, nlines)
    else: return lines

def get_title(bag, numw = 3):
    if numw > 0:
        r = SystemRandom().randint(0,len(bag))
        w = [bag[r]]
        return w + get_title(bag,numw - 1)
    else: return []

title = " ".join(get_title(bag_of_words))
lines = create_lines(bag_of_words)

text = "\n".join(lines)

open('text.txt','w',encoding='utf-8').write(title + "\n\n" + text)
