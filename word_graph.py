from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from heapq import nlargest
from operator import itemgetter
import re

class Graph(object):

    def plot_word(self, word):
        #word = re.sub('[^A-Za-z0-9]+', '', word)
        
        
        words = dict(Counter(word.split()))

        words = sorted(words.items(), key=lambda x: x[1])
        #words = dict(map(reversed, words))
        words = dict(words)
        words = nlargest(10, words.iteritems(), key=itemgetter(1))
        words = dict(words)



        counter = words
        word_name = counter.keys()
        word_counts = counter.values()


        # Plot histogram using matplotlib bar().
        indexes = np.arange(len(word_name))
        width = 0.4
        plt.bar(indexes, word_counts, width)
        plt.xticks(indexes + width * 0.5, word_name)
        plt.xlabel('Words')
        plt.ylabel('Fequency')
        plt.title('Word Occurrence')
        plt.savefig("image.png")
        plt.show()
