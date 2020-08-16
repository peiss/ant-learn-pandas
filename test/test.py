import tensorflow as tf
import numpy as np

y_true = np.array([0, 1, 0, 1])
y_pred = np.array([[0.8], [0.7], [0.6], [0.5]])
# Using 'auto'/'sum_over_batch_size' reduction type.
bce = tf.keras.losses.BinaryCrossentropy(reduction="none")
data = bce(y_true, y_pred)
print(data)

