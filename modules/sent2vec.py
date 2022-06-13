from keras_bert import load_trained_model_from_checkpoint
import os

base_dir = 'bert_model'
config_path = os.path.join(base_dir, 'bert_config.json')
checkpoint_path = os.path.join(base_dir, 'bert_config.json')

bert = load_trained_model_from_checkpoint(config_path, checkpoint_path)
print(bert.summary())