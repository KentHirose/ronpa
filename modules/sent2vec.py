import numpy as np
from gensim.models.doc2vec import Doc2Vec

doc2vec = Doc2Vec.load("model/jawiki.doc2vec.dbow300d.model")

# import MeCab
# mecab = MeCab.Tagger("-Owakati")
# def tokenize(text):
#     wakati = MeCab.Tagger("-O wakati")
#     wakati.parse("")
#     return wakati.parse(text).strip().split()


# janome -------------
from janome.tokenizer import Tokenizer
def tokenize(text):
    t = Tokenizer()
    tokens = t.tokenize(text)
    docs=[]
    for token in tokens:
        docs.append(token.surface)
    return docs
# --------------------


def sent2vec(sentences: list) -> np.ndarray:
    """
    文章からベクトルを生成

    Args:
        sentences (list): 文章

    Returns:
        np.ndarray: ベクトル (n_sentences, n_dim)
    """
    vecs = [doc2vec.infer_vector(tokenize(sent)) for sent in sentences]
    return np.array(vecs)