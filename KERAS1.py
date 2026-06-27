import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# Load MNIST dataset
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()
print(f"Training data shape: {X_train.shape} | Test: {X_test.shape}")

# Visualize some sample images
plt.figure(figsize=(12, 2))
for i in range(12):
    plt.subplot(1, 12, i + 1)
    plt.imshow(X_train[i], cmap='gray')
    plt.axis('off')
    plt.title(str(y_train[i]), fontsize=12)
plt.suptitle("Sample MNIST Images", fontsize=16)
plt.show()

# Normalize the data
X_train = X_train / 255.0
X_test = X_test / 255.0

# Flatten 28x28 -> 784
X_train = X_train.reshape(-1, 28 * 28)
X_test = X_test.reshape(-1, 28 * 28)

# Build a simple neural network model
model = keras.Sequential([
    keras.layers.Dense(512, activation='relu', input_shape=(784,)),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(256, activation='relu'),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10, activation='softmax')
])

model.summary()

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(
    X_train, y_train,
    epochs=10,
    batch_size=128,
    validation_split=0.1,
    callbacks=[keras.callbacks.EarlyStopping(patience= 3, restore_best_weights=True)]
)

# Evaluate the model
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Test accuracy: {test_acc:.4f}")

# Plot training history
fig, ax = plt.subplots(1, 2, figsize=(12, 4))
ax[0].plot(history.history['accuracy'], label='Train Accuracy')
ax[0].plot(history.history['val_accuracy'], label='Validation Accuracy')
ax[0].set_title('Model Accuracy')
ax[0].legend()
ax[1].plot(history.history['loss'], label='Train Loss')
ax[1].plot(history.history['val_loss'], label='Validation Loss')
ax[1].set_title('Model Loss')
ax[1].legend()
plt.tight_layout()
plt.show()

# See the predictions

predictions = model.predict(X_test[:15])
pred_classes = np.argmax(predictions, axis=1)

plt.figure(figsize=(15, 3))
for i in range(15):
    plt.subplot(1, 15, i + 1)
    plt.imshow(X_test[i].reshape(28, 28), cmap='gray')
    correct = pred_classes[i] == y_test[i]
    plt.title(f"Predicted: {pred_classes[i]}\nActual: {y_test[i]}", fontsize=12)
    plt.axis('off')
plt.suptitle("Green: Correct, Red: Incorrect", fontsize=16)
plt.show()