# import random 
# import re
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
# from sklearn import cluster, preprocessing, mixture
from sklearn import mixture

# def clustering(X: np.ndarray) -> np.ndarray:
#     """クラスタリング. k-means?"""
#     k = int(X.shape[0]/8)
#     X_size,n_features = X.shape
#     centroids  = X[np.random.choice(X_size,k)]
#     new_centroids = np.zeros((k, n_features))
#     cluster = np.zeros(X_size)
#     for epoch in range(350):
#         for i in range(X_size):
#             distances = np.sum((centroids - X[i]) ** 2, axis=1)
#             cluster[i] = np.argsort(distances)[0]
#         for j in range(k):
#             new_centroids[j] = X[cluster==j].mean(axis=0)
#         if np.sum(new_centroids == centroids) == k:
#             print("break")
#             break
#         centroids =  new_centroids
#     return cluster

def clustering(X: np.ndarray) -> np.ndarray:
    """クラスタリング. VBGMM"""
    vbgm = mixture.BayesianGaussianMixture(n_components=10)
    vbgm = vbgm.fit(X)
    cluster = vbgm.predict(X)
    return cluster

def pca(data: np.ndarray) -> np.ndarray:
    """次元削減"""
    pca=PCA(n_components=2)
    data=pca.fit_transform(data)
    return data

def normalize(X: np.ndarray) -> np.ndarray:
    """"0~100に正規化"""
    return MinMaxScaler((0, 100)).fit_transform(X)

def intervel(data: np.ndarray) -> np.ndarray:
    """間隔を調整する"""
    for seq in range (100):
        for i in range(data.shape[0]):
            for j in range(data.shape[0]):
                if i!=j:
                    while data[i][1]-data[j][1]<3 and data[i][1]-data[j][1]>=0:
                        data[i][1]+=0.1
                    while data[i][1]-data[j][1]>-3 and data[i][1]-data[j][1]<0:
                        data[i][1]-=0.1
    return data

def lang_judg(search_results_list: list) -> list:
    """アブストラクトが英語かどうかを判定し、英語だった場合タイトルに置き換える"""

    # 前回送ってくれたやつ (動かなかった) ----------------------------------------------
    # deliete = re.compile('[!"#$%&\'\\\\()*+,-./:;<=>?@[\\]^_`{|}~「」〔〕""〈〉『』【】＆＊・（）＄＃＠。、？！｀＋￥％]')
    # cleaned_text = list(deliete.sub('', search_results_list[2]))
    # num = int(len(cleaned_text)* 0.3)
    # nums = random.randint(0,(len(cleaned_text)-1))
    # count = 0
    # word_count = 0
    # while word_count <= num:
    #     judge_word = cleaned_text[nums]
    #     ans = re.match('^[a-zA-Z]+$', judge_word)
    #     cleaned_text.pop(nums)
    #     print(cleaned_text)
    #     if ans != 'None':
    #         count += 1
    #         word_count += 1
    #     elif ans == "None":
    #         word_count += 1
    # if count > int(num/2):
    #     search_results_list[2] = search_results_list[0]
    # -----------------------------------------------------------------

    # 何らかの処理

    return search_results_list

def make_balloon(writer, additional):
    return [f'著者:{w}\n\n{add}' for w, add in zip(writer, additional)]