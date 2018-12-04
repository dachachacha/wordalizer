import os
import collections
from random import shuffle, SystemRandom

sysrand = SystemRandom()

def frandom():
    ret = sysrand.random()
    for i in range(sysrand.randint(1,100)):       
        ret = ret * sysrand.random()
    return ret

def rshuffle(bag):
    for i in range(sysrand.randint(1,5)):
        shuffle(bag,frandom)

def avoid(fname):
    if fname in ['.DS_Store']: return True
    else: return False

files = {}

counter_of_words = collections.Counter()
bag_of_words = []

for i in os.listdir('./diary/'):
    if (avoid(i)) : continue
    if i.endswith('.txt') or i == 'shrooms':
        print(i)
        #lines = open('diary/' + i,'rb').readlines()
        sentences = [ x.strip() for x in open('diary/' + i,encoding='utf-8').readlines() ]
        files[i] =  " ".join([x.strip() for x in [ " ".join(x.split()) for x in sentences ]])
        elements = [ x.strip() for x in files[i].split(" ") ]
        rshuffle(elements)
        counter_of_words.update(elements)
        bag_of_words.extend(elements)
    if i == 'diary_end_7_2016':
        files[i] = {}
        files[i]['dir'] = i
        files[i]['files'] = {}
        for j in os.listdir('diary/' + i):
            if (avoid(j)) : continue
            print ("processing: " + j)
            sentences = [ x.strip() for x in open('diary/' + i + '/' + j,encoding='utf-8').readlines() ]
            files[i]['files'][j] = " ".join([ x.strip() for x in [ " ".join(x.split()) for x in sentences ]])
            elements = [ x.strip() for x in files[i]['files'][j].split(" ") ]
            rshuffle(elements)
            bag_of_words.extend(elements)
            counter_of_words.update(elements)

for i in files.keys():
    print(i)
    if type(files[i]) == dict:
        for j in files[i]['files'].keys():
            print('\t' + j)

rshuffle(bag_of_words)
#print(counter_of_words)

keys = list(dict(counter_of_words).keys())
counter_of_words2 = {}
rshuffle(keys)
for i in keys:
    counter_of_words2[i] = counter_of_words[i]

import json
with open('wordcount.json', 'w', encoding='utf-8') as fp:
    json.dump(counter_of_words2, fp, indent=4, sort_keys=True, ensure_ascii=False)
with open('words.txt', 'w', encoding='utf-8') as fp:
    for i in bag_of_words:
        fp.write("%s\n" % i)
#print(counter_of_words)
