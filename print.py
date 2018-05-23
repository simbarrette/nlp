from stat_parser import Parser
parsed = Parser().parse('Il était une fois un petit chien.')
print (parsed)
parsed.pretty_print()
# import nltk
# import operator
# import os
# import pickle
# import random
# import re
# import codecs
# import sys
# from nltk.tree import Tree
# from collections import defaultdict
# from tqdm import tqdm
# from stat_parser import Parser

# with codecs.open('text.txt', encoding='utf-8') as corpus:
#             sents = nltk.sent_tokenize(corpus.read())
#             print("Testint printing my own corpus")
#             print(sents)

# sents = nltk.corpus.gutenberg.sents('austen-emma.txt')
# print("Testint the print of austen-emma")
# print(sents)