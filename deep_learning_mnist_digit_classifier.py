import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# 1. Load the MNIST dataset (handwritten digits)
print("Loading data...")
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 2. Normalize pixels to be between 0 and 1
x_train, x_test = x_train / 255.0, x_test / 255.0

# 3. Build a Simple Neural Network (Sequential)
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)), # Flattens the 28x28 image to a vector
    layers.Dense(128, activation='relu'), # Hidden layer with 128 neurons
    layers.Dropout(0.2),                  # Prevents overfitting
    layers.Dense(10, activation='softmax') # Output layer for 10 digits (0-9)
])

# 4. Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 5. Train the model
print("\nTraining the model...")
model.fit(x_train, y_train, epochs=5)

# 6. Evaluate and show a prediction
loss, acc = model.evaluate(x_test, y_test, verbose=2)
print(f"\nTest Accuracy: {acc*100:.2f}%")

# Plot one prediction to verify
plt.imshow(x_test[0], cmap='gray')
plt.title(f"Predicted Label: {model.predict(x_test[:1]).argmax()}")
plt.show()