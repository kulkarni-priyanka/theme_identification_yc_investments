import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from model import *
from utils import *
import pandas as pd
import pickle
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore', category=Warning)

import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--fpath', default='E:/ACM_Stuff_v2/625.726/Project/contextual_topic_identification-master/contextual_topic_identification-master/data/yc2.csv')
    parser.add_argument('--ntopic', default=4)
    parser.add_argument('--method', default='TFIDF')
    parser.add_argument('--samp_size', default=2585)
    args = parser.parse_args()

    data = pd.read_csv(str(args.fpath))
    data = data.fillna('')  # only the comments has NaN's
    #rws = data.review
    rws = data.Description
    sentences, token_lists, idx_in = preprocess(rws, samp_size=int(args.samp_size))
    # Define the topic model object
    met = ['TFIDF', 'LDA', 'BERT', 'LDA_BERT']
    for method in met:
        print("Method: ",method)
        tm = Topic_Model(k = int(args.ntopic), method = str(method))
        # Fit the topic model by chosen method
        tm.fit(sentences, token_lists)
        # Evaluate using metrics
        with open("E:/ACM_Stuff_v2/625.726/Project/contextual_topic_identification-master/contextual_topic_identification-master/docs/saved_models/yc_{}.file".format(method), "wb") as f:
            pickle.dump(tm, f, pickle.HIGHEST_PROTOCOL)

        print('Coherence UMass:', get_coherence(tm, token_lists, 'u_mass'))
        print('Coherence CV:', get_coherence(tm, token_lists, 'c_v'))
        print('Silhouette Score:', get_silhouette(tm))
        # visualize and save img
        visualize(tm)
        for i in range(tm.k):
            get_wordcloud(tm, token_lists, i)
