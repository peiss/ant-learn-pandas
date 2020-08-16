import tensorflow as tf
import numpy as np

print(tf.__version__)

x = np.random.rand(9, 3)
y = np.random.randint(2, size=(9,))
print(x, y)

ds = tf.data.Dataset.from_tensor_slices((x, y)).batch(3)
for row in ds:
    print(row)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(3, activation='relu', input_shape=(3,)),
    tf.keras.layers.Dense(1, activation='sigmoid')]
)

model.compile(optimizer='sgd', loss=tf.keras.losses.BinaryCrossentropy())

model.fit(ds)
model.evaluate(ds)
result = model.predict(ds)
for row in ds:
    y_true = row[1]
    print(y_true)
print(result)
