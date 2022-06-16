import numpy as np
from gensim.models.doc2vec import Doc2Vec
import MeCab

doc2vec = Doc2Vec.load("model/jawiki.doc2vec.dbow300d.model")
mecab = MeCab.Tagger("-Owakati")

# ------
from janome.tokenizer import Tokenizer
def sep_by_janome(text):
    t = Tokenizer()
    tokens = t.tokenize(text)
    docs=[]
    for token in tokens:
        docs.append(token.surface)
    return docs
# -------


def sent2vec(sentences: list) -> np.ndarray:
    """
    文章からベクトルを生成

    Args:
        sentences (list): 文章

    Returns:
        np.ndarray: ベクトル (n_sentences, n_dim)
    """
    vecs = [doc2vec.infer_vector(sep_by_janome(sent)) for sent in sentences]
    return np.array(vecs)