# -*- coding: utf-8 -*-
"""Luthfi_20110010_tfidf

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hv6tFEwptFqBoyPs9tDE1Ee0Bt_yGImW

## LUTHFI RAKAN
## 20110010

## Tugas Praktikum
##load dataset yang diberikan menjadi dataframe
##ubah kolom "content" menjadi vector menggunakan TFIDFVectorizer dan tampilkan hasilnya
## Tampilkan nama fiturnya mengunakan get_features_name_out
"""

!pip install luwiji

import numpy as np
import pandas as pd
import os
from luwiji.text_proc import illustration
from nltk.tokenize import word_tokenize
from tqdm.auto import tqdm
from gensim.models import Word2Vec
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer

text = ['Ini adalah pensil',
        'Ini adalah pulpen saya dan ini pulpen dia',
        'Saya beli pensil ini',
        'Saya beli pulpen itu']
text

"""## Bag of Word"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('Bag of Words.png')

plt.imshow(img)
plt.axis('off')
plt.show()

bow = CountVectorizer()
bow_matrix = bow.fit_transform(text)

bow_matrix

pd.DataFrame(bow_matrix.toarray(), columns=bow.get_feature_names_out(), index=text)

"""## Inverse Document Frequency (IDF)"""

illustration.inverse_df

"""## Term Frequency - Inverse Document Frequency (TF-IDF)"""

tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(text)

print(tfidf_matrix)

tfidf.get_feature_names_out()

pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf.get_feature_names_out(), index=text)

"""kelemahan BoW dan TF-IDF:
- urutan ngga ngaruh buat pembobotannya
"""

df = pd.read_csv('hasil_saya (1).csv')
df = df.drop(columns='Unnamed: 0')
df.head()

sent = [word_tokenize(content.lower()) for content in tqdm(df.content)]

sent

tfidf.get_feature_names_out()

"""# Word2Vec"""

# size = neuron
# window = berapa lihat kanan kirinya
# min_count = min berapa kali kata muncul baru dianggap vocab
# workers = jumlah cpu
# iter = epoch
# sg = skipgram (kalau 1 akan pake cbow) default = 0
model = Word2Vec(sent, size=128, window=5, min_count=3, workers=8, iter=1000, sg=0)

os.makedirs("model/w2v/", exist_ok=True)

model.save("model/w2v/review.w2v")



