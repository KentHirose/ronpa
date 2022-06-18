import sys; sys.path.insert(0, './modules')
from paper_search import search
from sent2vec import sent2vec
from tours import pca, clustering, normalize, intervel

def flow(query, n_papers=20):
    titles, links, abstracts = search(query, n_papers)
    vectors = sent2vec(abstracts)
    vectors_2d = pca(vectors)
    positions = normalize(vectors_2d)
    positions = intervel(positions)
    clusters = clustering(vectors)
    return titles, links, positions, clusters