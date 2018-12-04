import sys
from random import shuffle, SystemRandom

sysrand = SystemRandom()

def frandom():
    ret = sysrand.random()
    for i in range(sysrand.randint(1,100)):
        ret = ret * sysrand.random()
    return ret

def rshuffle(bag):
    for i in range(sysrand.randint(1,10)):
        shuffle(bag,frandom)

words_per_line = 15
char_per_line = 55
lines_per_page = 35
bag_of_words = open('words.txt',encoding='utf-8').read().split("\n")
rshuffle(bag_of_words)
cnt = 0
line = []
lines = []
char_cnt = 0
line_cnt = 0
for i in bag_of_words:
    char_cnt += len(i)
    cnt += 1
    line.append(i)
    #if cnt == words_per_line or char_cnt > char_per_line:
    if char_cnt > char_per_line:
        char_cnt = 0
        cnt = 0
        lines.append(" ".join(line))
        line = []
        line_cnt += 1
    if line_cnt > lines_per_page:
        lines.append("")
        line_cnt = 0

text = "\n".join(lines)
title = []
for i in range(3):
    r = SystemRandom().randint(0,len(bag_of_words))
    title.append(bag_of_words[r])
import string
title = " ".join(title)
translator = title.maketrans('', '', string.punctuation)
title = title.translate(translator)
open('text.txt','w',encoding='utf-8').write(title + "\n\n" + text)
    
#quit()
#for i in lines:
#    print(i)
#    #sys.stdout.buffer.write(i.encode())
