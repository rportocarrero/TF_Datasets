import tensorflow as tf
import tensorflow-datasets as tfds

print(tf.__version__)

ds = tfds.load('places365_small', split='train', shuffle_files=True)
