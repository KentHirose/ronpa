import json
import sys; sys.path.insert(0, './modules')
from paper_search import search
from sent2vec import sent2vec
from tours import pca, clustering, normalize, intervel

with open('config.json') as f:
    config = json.load(f)

colors_rgb = config['colors_rgb']
query_text = config['query_text']
document_type_list = query_text['document_type']
category_list = query_text['category']

def flow(search_options: dict):
    titles, links, abstracts = search(
        **search_options,
        document_type_list=document_type_list,
        category_list=category_list
        )
    vectors = sent2vec(abstracts)
    vectors_2d = pca(vectors)
    positions = normalize(vectors_2d)
    positions = intervel(positions)
    positions = normalize(positions)
    clusters = clustering(vectors)
    colors = [colors_rgb[int(c)] for c in clusters]
    return titles, links, positions, colors