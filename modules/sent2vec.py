import numpy as np
from gensim.models import KeyedVectors

model_dir = './entity_vector/entity_vector.model.bin'
model = KeyedVectors.load_word2vec_format(model_dir, binary=True)

