import csv
import encodings
import tensorflow as tf
import numpy
from sklearn.model_selection import train_test_split

# Read data in from file
with open("neuralsamples.txt", encoding='utf-8') as f:
    f.readline() #removing the first line of samples
    lines = f.readlines();
    # print(lines)
    data = []
    for line in lines:
        x, y = line.split(',')
        if len(y) > 1:
            y = y[:-1]
        data.append({
            "evidence": [ord(i) for i in x],
            "label": 1 if y == "1" else 0
        })
    print(data)

# Separate data into training and testing groups
evidence = [row["evidence"] for row in data]
labels = [row["label"] for row in data]
X_training, X_testing, y_training, y_testing = train_test_split(
    evidence, labels, train_size=1
)

# Create a neural network
model = tf.keras.models.Sequential()
for i in range(5):
    print(1)
# Add a hidden layer with 8 units, with ReLU activation
model.add(tf.keras.layers.Dense(8, activation="relu"))

# Add a hidden layer with 8 units, with ReLU activation
model.add(tf.keras.layers.Dense(8, activation="relu"))

# # Add output layer with 1 unit, with sigmoid activation
model.add(tf.keras.layers.Dense(1, activation="sigmoid"))

# Train neural network
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)
print(X_training)
print(y_training)
model.fit(X_training, y_training, epochs=20)

# # Evaluate how well model performs
# model.evaluate(X_testing, y_testing, verbose=2)
# print(X_training[0])
inp = [ord(i) for i in input()]
print(inp)
print(X_training[0])

ou = model.predict([inp]);
print(ou[0][0])