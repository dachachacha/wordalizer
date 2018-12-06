import os
import collections
from random import shuffle, SystemRandom

def avoid(fname):
    if fname in ['.DS_Store']: return True
    else: return False

def tokenize(line):
    return [ x.strip() for x in line.split() if x.strip() ]

def get_file_contents(folder):
    tokens = []
    for i in os.listdir(folder):
        if avoid(i): continue
        path = os.path.join(folder,i)
        if os.path.isdir(path):
            tokens += get_file_contents(path)
        else:
            tokens += tokenize(open(path, encoding='utf-8').read())
    return tokens

tokens = get_file_contents('diary')
shuffle(tokens,SystemRandom().random)
words = " ".join(tokens)
counter = collections.Counter()
counter.update(tokens)

import json
with open('wordcount.json', 'w', encoding='utf-8') as fp:
    json.dump(counter, fp, indent=4, sort_keys=True, ensure_ascii=False)        

