from sklearn import cluster
from search import paper_search
from sent2vec import sent2vec
from tours import pca, clustering

def main(query, n_papers=20):
    titles, links, abstracts = paper_search(query, n_papers)
    vectors = sent2vec(abstracts)
    positions = pca(vectors)
    clusters = clustering(vectors)
    return titles, links, positions, clusters


