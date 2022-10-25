import tensorflow as tf
import tensorflow_datasets as tfds

print(tf.__version__)
print(tfds.list_builders())
ds = tfds.load('places365_small', split='train', shuffle_files=True)
