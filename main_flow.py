import sys; sys.path.insert(0, './modules')
from paper_search import search
from sent2vec import sent2vec
from tours import pca, clustering, normalize

def flow(query, n_papers=20):
    titles, links, abstracts = search(query, n_papers)
    vectors = sent2vec(abstracts)
    positions = pca(vectors)
    positions = normalize(positions)
    clusters = clustering(vectors)
    return titles, links, positions, clusters