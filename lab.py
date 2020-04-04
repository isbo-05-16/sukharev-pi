import pymorphy2
import re

from sys import argv
from collections import Counter

morph = pymorphy2.MorphAnalyzer()

def count(text):
    text = re.sub(r'[^\w\s]','', text)
    words = text.split()
    pos_gen = (morph.parse(word)[0].tag.POS for word in words)
    c = Counter(pos_gen)
    return (c['ADJF'] + c['ADJS'], c['ADVB'], c['VERB'] + c['INFN'])


if __name__ == "__main__":
    with open(argv[-1], 'r') as f:
        data = f.read()
        print('прилагательных: {0}, наречий: {1}, глаголов: {2}'.format(*count(data)))
