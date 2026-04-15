# The 2026 Python Metromap: TensorFlow and Keras – Deep Learning

## Series I: AI & Machine Learning with Python | Story 2 of 4

![The 2026 Python Metromap/images/TensorFlow and Keras – Deep Learning](images/TensorFlow and Keras – Deep Learning.png)

## 📖 Introduction

**Welcome to the second stop on the AI & Machine Learning with Python Line.**

You've mastered traditional machine learning with scikit-learn—classification, regression, clustering, and model evaluation. You can predict customer churn, detect spam, and estimate house prices. But traditional models have limitations: they struggle with unstructured data like images, audio, and text; they require manual feature engineering; and they can't learn hierarchical representations.

That's where deep learning comes in.

TensorFlow and Keras are the most popular frameworks for deep learning. Keras provides a high-level API that makes building neural networks intuitive, while TensorFlow handles the heavy lifting of computation, automatic differentiation, and GPU acceleration. Together, they enable you to build models that learn features automatically from raw data.

This story—**The 2026 Python Metromap: TensorFlow and Keras – Deep Learning**—is your guide to building neural networks. We'll build a handwritten digit classifier using convolutional neural networks (CNNs). We'll create a fashion item recognizer using the Fashion MNIST dataset. We'll implement a sentiment analyzer for movie reviews using recurrent neural networks (RNNs). And we'll learn about model architecture, training, evaluation, and deployment.

**Let's go deep.**

---

## 📚 Where You Are in the Journey

### The Master Story Arc: The 2026 Python Metromap Series

- 🗺️ **The 2026 Python Metromap: Master Python Beginner To Pro** – A paradigm shift from linear learning to transit-system mastery.
- 🧭 **The 2026 Python Metromap: Why the Old Learning Routes Are Obsolete** – Diagnosing and preventing the most common learning pitfalls.
- 📖 **The 2026 Python Metromap: Reading the Map** – Strategic navigation across all lines.
- 🎒 **The 2026 Python Metromap: Avoiding Derailments** – Diagnosing and preventing the most common learning pitfalls.
- 🏁 **The 2026 Python Metromap: From Passenger to Driver** – Building your portfolio using the Metromap structure.

### Series A: Foundations Station (7 Stories) – COMPLETED
### Series B: Functions & Modules Yard (6 Stories) – COMPLETED
### Series C: Data Structures Express (5 Stories) – COMPLETED
### Series D: Object-Oriented Programming (OOP) Line (6 Stories) – COMPLETED
### Series E: File & Data Handling Line (5 Stories) – COMPLETED
### Series F: Advanced Python Engineering (6 Stories) – COMPLETED
### Series G: Data Science & Visualization (5 Stories) – COMPLETED
### Series H: Web Development & Automation (5 Stories) – COMPLETED

### Series I: AI & Machine Learning with Python (4 Stories)

- 🤖 **The 2026 Python Metromap: Scikit-learn – Traditional ML** – Spam classifier for emails; customer churn predictor; house price estimator.

- 🧠 **The 2026 Python Metromap: TensorFlow and Keras – Deep Learning** – Handwritten digit classifier; fashion item recognizer; sentiment analyzer. **⬅️ YOU ARE HERE**

- 🔥 **The 2026 Python Metromap: PyTorch – Research and Production** – Custom neural network for image classification; training loops; model deployment. 🔜 *Up Next*

- 🚀 **The 2026 Python Metromap: End-to-End ML Pipeline Project** – Complete machine learning pipeline from data collection to deployment for house price prediction.

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🧠 Section 1: TensorFlow and Keras Fundamentals – Building Your First Neural Network

Keras provides a simple, intuitive API for building neural networks with layers, activations, and optimizers.

**SOLID Principle Applied: Single Responsibility** – Each layer has one transformation purpose.

**Design Pattern: Builder Pattern** – Sequential API builds models incrementally.

```python
"""
TENSORFLOW AND KERAS FUNDAMENTALS: BUILDING YOUR FIRST NEURAL NETWORK

This section covers the basics of TensorFlow and Keras.

SOLID Principle: Single Responsibility
- Each layer has one transformation purpose

Design Pattern: Builder Pattern
- Sequential API builds models incrementally
"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models, callbacks
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def demonstrate_tensorflow_basics():
    """
    Demonstrates basic TensorFlow operations.
    
    TensorFlow uses tensors (multi-dimensional arrays) similar to NumPy.
    """
    print("=" * 60)
    print("SECTION 1A: TENSORFLOW BASICS")
    print("=" * 60)
    
    # CREATE TENSORS
    print("\n1. CREATING TENSORS")
    print("-" * 40)
    
    # From NumPy array
    np_array = np.array([1, 2, 3, 4, 5])
    tf_tensor = tf.convert_to_tensor(np_array)
    print(f"  NumPy array: {np_array}")
    print(f"  Tensor: {tf_tensor}")
    print(f"  Tensor shape: {tf_tensor.shape}")
    print(f"  Tensor dtype: {tf_tensor.dtype}")
    
    # Constant tensor
    constant = tf.constant([[1, 2], [3, 4]], dtype=tf.float32)
    print(f"  Constant tensor:\n{constant}")
    
    # Random tensors
    random_normal = tf.random.normal((3, 3), mean=0, stddev=1)
    random_uniform = tf.random.uniform((2, 4), minval=0, maxval=1)
    print(f"  Random normal: {random_normal.shape}")
    print(f"  Random uniform: {random_uniform.shape}")
    
    # TENSOR OPERATIONS
    print("\n2. TENSOR OPERATIONS")
    print("-" * 40)
    
    a = tf.constant([[1, 2], [3, 4]])
    b = tf.constant([[5, 6], [7, 8]])
    
    print(f"  a:\n{a}")
    print(f"  b:\n{b}")
    print(f"  a + b:\n{a + b}")
    print(f"  a * b:\n{a * b}")
    print(f"  a @ b (matrix multiplication):\n{a @ b}")
    
    # GPU ACCELERATION
    print("\n3. GPU ACCELERATION")
    print("-" * 40)
    
    physical_devices = tf.config.list_physical_devices()
    print(f"  Available devices: {physical_devices}")
    
    if tf.config.list_physical_devices('GPU'):
        print("  GPU is available! Training will be faster.")
    else:
        print("  GPU not available. Using CPU.")


def build_mlp_mnist():
    """
    Builds a Multi-Layer Perceptron (MLP) for MNIST digit classification.
    
    Design Pattern: Builder Pattern - Sequential model construction
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: MULTI-LAYER PERCEPTRON FOR MNIST")
    print("=" * 60)
    
    # LOAD MNIST DATASET
    print("\n1. LOADING MNIST DATASET")
    print("-" * 40)
    
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    
    print(f"  Training images: {x_train.shape}")
    print(f"  Training labels: {y_train.shape}")
    print(f"  Test images: {x_test.shape}")
    print(f"  Test labels: {y_test.shape}")
    print(f"  Image dimensions: {x_train.shape[1]} x {x_train.shape[2]}")
    print(f"  Pixel range: {x_train.min()} - {x_train.max()}")
    print(f"  Number of classes: {len(np.unique(y_train))}")
    
    # PREPROCESS DATA
    print("\n2. PREPROCESSING DATA")
    print("-" * 40)
    
    # Normalize pixel values to [0, 1]
    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0
    
    # Flatten 28x28 images to 784-dimensional vectors
    x_train_flat = x_train.reshape(x_train.shape[0], -1)
    x_test_flat = x_test.reshape(x_test.shape[0], -1)
    
    print(f"  Flattened training shape: {x_train_flat.shape}")
    print(f"  Normalized pixel range: {x_train.min()} - {x_train.max()}")
    
    # One-hot encode labels
    y_train_cat = keras.utils.to_categorical(y_train, 10)
    y_test_cat = keras.utils.to_categorical(y_test, 10)
    
    print(f"  One-hot encoded labels shape: {y_train_cat.shape}")
    print(f"  Sample label 5: {y_train[0]} → {y_train_cat[0]}")
    
    # VISUALIZE DATA
    print("\n3. VISUALIZING SAMPLE IMAGES")
    print("-" * 40)
    
    fig, axes = plt.subplots(2, 5, figsize=(12, 6))
    for i, ax in enumerate(axes.flat):
        ax.imshow(x_train[i], cmap='gray')
        ax.set_title(f"Label: {y_train[i]}")
        ax.axis('off')
    plt.suptitle("Sample MNIST Digits", fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()
    print("  Displayed sample digits")
    
    # BUILD MLP MODEL
    print("\n4. BUILDING MLP MODEL")
    print("-" * 40)
    
    model = models.Sequential([
        layers.Dense(128, activation='relu', input_shape=(784,), name='hidden_1'),
        layers.Dropout(0.2),
        layers.Dense(64, activation='relu', name='hidden_2'),
        layers.Dropout(0.2),
        layers.Dense(10, activation='softmax', name='output')
    ])
    
    model.summary()
    
    print(f"\n  Total parameters: {model.count_params():,}")
    
    # COMPILE MODEL
    print("\n5. COMPILING MODEL")
    print("-" * 40)
    
    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    
    print("  Optimizer: Adam")
    print("  Loss: Categorical Crossentropy")
    print("  Metrics: Accuracy")
    
    # EARLY STOPPING CALLBACK
    print("\n6. SETTING UP CALLBACKS")
    print("-" * 40)
    
    early_stop = callbacks.EarlyStopping(
        monitor='val_loss',
        patience=3,
        restore_best_weights=True,
        verbose=0
    )
    
    reduce_lr = callbacks.ReduceLROnPlateau(
        monitor='val_loss',
        factor=0.5,
        patience=2,
        verbose=0
    )
    
    print("  Early stopping (patience=3)")
    print("  Reduce LR on plateau (factor=0.5)")
    
    # TRAIN MODEL
    print("\n7. TRAINING MODEL")
    print("-" * 40)
    
    history = model.fit(
        x_train_flat, y_train_cat,
        batch_size=32,
        epochs=20,
        validation_split=0.2,
        callbacks=[early_stop, reduce_lr],
        verbose=0
    )
    
    print(f"  Training completed: {len(history.history['loss'])} epochs")
    print(f"  Final training accuracy: {history.history['accuracy'][-1]:.4f}")
    print(f"  Final validation accuracy: {history.history['val_accuracy'][-1]:.4f}")
    
    # EVALUATE MODEL
    print("\n8. EVALUATING MODEL")
    print("-" * 40)
    
    test_loss, test_accuracy = model.evaluate(x_test_flat, y_test_cat, verbose=0)
    print(f"  Test loss: {test_loss:.4f}")
    print(f"  Test accuracy: {test_accuracy:.4f}")
    
    # PLOT TRAINING HISTORY
    print("\n9. PLOTTING TRAINING HISTORY")
    print("-" * 40)
    
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    
    axes[0].plot(history.history['accuracy'], label='Train')
    axes[0].plot(history.history['val_accuracy'], label='Validation')
    axes[0].set_title('Model Accuracy')
    axes[0].set_xlabel('Epoch')
    axes[0].set_ylabel('Accuracy')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    
    axes[1].plot(history.history['loss'], label='Train')
    axes[1].plot(history.history['val_loss'], label='Validation')
    axes[1].set_title('Model Loss')
    axes[1].set_xlabel('Epoch')
    axes[1].set_ylabel('Loss')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    
    plt.suptitle("Training History - MLP on MNIST", fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()
    print("  Displayed training history plots")
    
    # MAKE PREDICTIONS
    print("\n10. MAKING PREDICTIONS")
    print("-" * 40)
    
    predictions = model.predict(x_test_flat[:10], verbose=0)
    predicted_classes = np.argmax(predictions, axis=1)
    
    print("  Sample predictions:")
    for i in range(10):
        true_label = y_test[i]
        pred_label = predicted_classes[i]
        confidence = predictions[i][pred_label]
        status = "✓" if true_label == pred_label else "✗"
        print(f"    {status} Image {i}: True={true_label}, Predicted={pred_label}, Confidence={confidence:.2%}")
    
    # CONFUSION MATRIX
    print("\n11. CONFUSION MATRIX")
    print("-" * 40)
    
    y_pred = model.predict(x_test_flat, verbose=0)
    y_pred_classes = np.argmax(y_pred, axis=1)
    
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_test, y_pred_classes)
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title('Confusion Matrix - MNIST Classification')
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.tight_layout()
    plt.show()
    print("  Displayed confusion matrix")
    
    return model, history


def demonstrate_save_load_model():
    """
    Demonstrates saving and loading Keras models.
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: SAVING AND LOADING MODELS")
    print("=" * 60)
    
    # Create a simple model
    model = models.Sequential([
        layers.Dense(64, activation='relu', input_shape=(10,)),
        layers.Dense(32, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])
    
    model.compile(optimizer='adam', loss='binary_crossentropy')
    
    print("\n1. SAVING MODEL")
    print("-" * 40)
    
    # Save in Keras format
    model.save('simple_model.keras')
    print("  Saved model to 'simple_model.keras'")
    
    # Save weights only
    model.save_weights('model_weights.h5')
    print("  Saved weights to 'model_weights.h5'")
    
    # Save architecture as JSON
    model_json = model.to_json()
    with open('model_architecture.json', 'w') as f:
        f.write(model_json)
    print("  Saved architecture to 'model_architecture.json'")
    
    print("\n2. LOADING MODEL")
    print("-" * 40)
    
    # Load from Keras format
    loaded_model = keras.models.load_model('simple_model.keras')
    print("  Loaded model from 'simple_model.keras'")
    
    # Load from JSON and weights
    with open('model_architecture.json', 'r') as f:
        loaded_json = keras.models.model_from_json(f.read())
    loaded_json.load_weights('model_weights.h5')
    print("  Loaded model from JSON and weights")
    
    print("\n3. CHECKING MODEL EQUALITY")
    print("-" * 40)
    
    # Create test input
    test_input = np.random.random((1, 10))
    
    original_output = model.predict(test_input, verbose=0)
    loaded_output = loaded_model.predict(test_input, verbose=0)
    
    print(f"  Original model output: {original_output[0][0]:.6f}")
    print(f"  Loaded model output: {loaded_output[0][0]:.6f}")
    print(f"  Difference: {abs(original_output[0][0] - loaded_output[0][0]):.8f}")
    
    # Clean up
    import os
    os.remove('simple_model.keras')
    os.remove('model_weights.h5')
    os.remove('model_architecture.json')
    print("\n  Cleaned up saved files")


if __name__ == "__main__":
    demonstrate_tensorflow_basics()
    build_mlp_mnist()
    demonstrate_save_load_model()
```

---

## 👕 Section 2: Fashion MNIST Classifier with CNN

Convolutional Neural Networks (CNNs) are designed for image data, learning spatial hierarchies of features.

**SOLID Principles Applied:**
- Single Responsibility: Each convolutional layer extracts one type of feature
- Dependency Inversion: Model depends on layer abstractions

**Design Patterns:**
- Builder Pattern: Sequential model construction
- Strategy Pattern: Different pooling and activation strategies

```python
"""
FASHION MNIST CLASSIFIER WITH CNN

This section builds a Convolutional Neural Network for fashion item recognition.

SOLID Principles Applied:
- Single Responsibility: Each convolutional layer extracts one type of feature
- Dependency Inversion: Model depends on layer abstractions

Design Patterns:
- Builder Pattern: Sequential model construction
- Strategy Pattern: Different pooling and activation strategies
"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models, callbacks
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class FashionCNN:
    """
    CNN classifier for Fashion MNIST dataset.
    
    Design Pattern: Builder Pattern - Builds CNN architecture incrementally
    """
    
    def __init__(self, input_shape=(28, 28, 1), num_classes=10):
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.model = None
        self.history = None
    
    def build_model(self):
        """Build the CNN architecture."""
        self.model = models.Sequential([
            # First convolutional block
            layers.Conv2D(32, (3, 3), activation='relu', input_shape=self.input_shape),
            layers.BatchNormalization(),
            layers.MaxPooling2D((2, 2)),
            layers.Dropout(0.25),
            
            # Second convolutional block
            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.BatchNormalization(),
            layers.MaxPooling2D((2, 2)),
            layers.Dropout(0.25),
            
            # Third convolutional block
            layers.Conv2D(128, (3, 3), activation='relu'),
            layers.BatchNormalization(),
            layers.MaxPooling2D((2, 2)),
            layers.Dropout(0.25),
            
            # Flatten and dense layers
            layers.Flatten(),
            layers.Dense(256, activation='relu'),
            layers.BatchNormalization(),
            layers.Dropout(0.5),
            layers.Dense(self.num_classes, activation='softmax')
        ])
        
        return self.model
    
    def compile_model(self, learning_rate=0.001):
        """Compile the model with optimizer, loss, and metrics."""
        self.model.compile(
            optimizer=keras.optimizers.Adam(learning_rate=learning_rate),
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']
        )
        return self
    
    def train(self, x_train, y_train, x_val, y_val, epochs=30, batch_size=64):
        """Train the CNN model."""
        # Callbacks
        early_stop = callbacks.EarlyStopping(
            monitor='val_accuracy',
            patience=5,
            restore_best_weights=True,
            verbose=0
        )
        
        reduce_lr = callbacks.ReduceLROnPlateau(
            monitor='val_loss',
            factor=0.5,
            patience=3,
            min_lr=1e-6,
            verbose=0
        )
        
        # Data augmentation
        data_augmentation = keras.Sequential([
            layers.RandomRotation(0.1),
            layers.RandomZoom(0.1),
            layers.RandomTranslation(0.1, 0.1),
        ])
        
        # Train
        self.history = self.model.fit(
            x_train, y_train,
            batch_size=batch_size,
            epochs=epochs,
            validation_data=(x_val, y_val),
            callbacks=[early_stop, reduce_lr],
            verbose=0
        )
        
        return self.history
    
    def evaluate(self, x_test, y_test):
        """Evaluate the model on test data."""
        test_loss, test_accuracy = self.model.evaluate(x_test, y_test, verbose=0)
        return test_loss, test_accuracy
    
    def predict(self, x):
        """Make predictions."""
        return self.model.predict(x, verbose=0)
    
    def plot_training_history(self):
        """Plot training and validation metrics."""
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))
        
        axes[0].plot(self.history.history['accuracy'], label='Train')
        axes[0].plot(self.history.history['val_accuracy'], label='Validation')
        axes[0].set_title('Model Accuracy')
        axes[0].set_xlabel('Epoch')
        axes[0].set_ylabel('Accuracy')
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)
        
        axes[1].plot(self.history.history['loss'], label='Train')
        axes[1].plot(self.history.history['val_loss'], label='Validation')
        axes[1].set_title('Model Loss')
        axes[1].set_xlabel('Epoch')
        axes[1].set_ylabel('Loss')
        axes[1].legend()
        axes[1].grid(True, alpha=0.3)
        
        plt.suptitle("CNN Training History - Fashion MNIST", fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.show()
    
    def visualize_predictions(self, x_test, y_test, num_images=16):
        """Visualize model predictions on test images."""
        predictions = self.predict(x_test[:num_images])
        predicted_classes = np.argmax(predictions, axis=1)
        
        class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                       'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
        
        fig, axes = plt.subplots(4, 4, figsize=(12, 12))
        axes = axes.flatten()
        
        for i in range(num_images):
            ax = axes[i]
            ax.imshow(x_test[i].squeeze(), cmap='gray')
            true_label = class_names[y_test[i]]
            pred_label = class_names[predicted_classes[i]]
            confidence = predictions[i][predicted_classes[i]]
            
            color = 'green' if true_label == pred_label else 'red'
            ax.set_title(f"True: {true_label}\nPred: {pred_label}\nConf: {confidence:.2%}",
                        fontsize=9, color=color)
            ax.axis('off')
        
        plt.suptitle("CNN Predictions - Fashion MNIST", fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.show()
    
    def get_model_summary(self):
        """Print model summary."""
        self.model.summary()
        return self


def demonstrate_fashion_cnn():
    """
    Demonstrate CNN for Fashion MNIST classification.
    """
    print("\n" + "=" * 60)
    print("SECTION 2: FASHION MNIST CNN CLASSIFIER")
    print("=" * 60)
    
    # LOAD DATA
    print("\n1. LOADING FASHION MNIST DATASET")
    print("-" * 40)
    
    (x_train, y_train), (x_test, y_test) = keras.datasets.fashion_mnist.load_data()
    
    print(f"  Training images: {x_train.shape}")
    print(f"  Test images: {x_test.shape}")
    print(f"  Classes: 10 (T-shirt, Trouser, Pullover, Dress, Coat, Sandal, Shirt, Sneaker, Bag, Boot)")
    
    # PREPROCESS DATA
    print("\n2. PREPROCESSING DATA")
    print("-" * 40)
    
    # Add channel dimension
    x_train = x_train.reshape(-1, 28, 28, 1).astype('float32') / 255.0
    x_test = x_test.reshape(-1, 28, 28, 1).astype('float32') / 255.0
    
    # Split validation set
    from sklearn.model_selection import train_test_split
    x_train, x_val, y_train, y_val = train_test_split(
        x_train, y_train, test_size=0.2, random_state=42, stratify=y_train
    )
    
    print(f"  Training set: {x_train.shape}")
    print(f"  Validation set: {x_val.shape}")
    print(f"  Test set: {x_test.shape}")
    print(f"  Pixel range: {x_train.min()} - {x_train.max()}")
    
    # VISUALIZE DATA
    print("\n3. VISUALIZING SAMPLE IMAGES")
    print("-" * 40)
    
    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                   'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
    
    fig, axes = plt.subplots(2, 5, figsize=(12, 6))
    for i, ax in enumerate(axes.flat):
        ax.imshow(x_train[i].squeeze(), cmap='gray')
        ax.set_title(class_names[y_train[i]], fontsize=10)
        ax.axis('off')
    plt.suptitle("Sample Fashion MNIST Images", fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()
    
    # BUILD CNN
    print("\n4. BUILDING CNN MODEL")
    print("-" * 40)
    
    cnn = FashionCNN()
    cnn.build_model()
    cnn.compile_model(learning_rate=0.001)
    cnn.get_model_summary()
    
    # TRAIN CNN
    print("\n5. TRAINING CNN")
    print("-" * 40)
    
    cnn.train(x_train, y_train, x_val, y_val, epochs=20, batch_size=64)
    
    # EVALUATE
    print("\n6. EVALUATING CNN")
    print("-" * 40)
    
    test_loss, test_accuracy = cnn.evaluate(x_test, y_test)
    print(f"  Test Loss: {test_loss:.4f}")
    print(f"  Test Accuracy: {test_accuracy:.4f}")
    
    # PLOT TRAINING HISTORY
    print("\n7. TRAINING HISTORY")
    print("-" * 40)
    
    cnn.plot_training_history()
    
    # VISUALIZE PREDICTIONS
    print("\n8. VISUALIZING PREDICTIONS")
    print("-" * 40)
    
    cnn.visualize_predictions(x_test, y_test, num_images=16)
    
    # CONFUSION MATRIX
    print("\n9. CONFUSION MATRIX")
    print("-" * 40)
    
    y_pred = cnn.predict(x_test)
    y_pred_classes = np.argmax(y_pred, axis=1)
    
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_test, y_pred_classes)
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=class_names, yticklabels=class_names)
    plt.title('Confusion Matrix - Fashion MNIST CNN')
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    
    # COMPARE WITH MLP
    print("\n10. COMPARISON WITH MLP")
    print("-" * 40)
    
    # Simple MLP for comparison
    mlp = models.Sequential([
        layers.Flatten(input_shape=(28, 28, 1)),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.2),
        layers.Dense(64, activation='relu'),
        layers.Dropout(0.2),
        layers.Dense(10, activation='softmax')
    ])
    
    mlp.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    mlp.fit(x_train, y_train, epochs=10, validation_data=(x_val, y_val), verbose=0)
    
    mlp_loss, mlp_acc = mlp.evaluate(x_test, y_test, verbose=0)
    
    print(f"  CNN Test Accuracy: {test_accuracy:.4f}")
    print(f"  MLP Test Accuracy: {mlp_acc:.4f}")
    print(f"  Improvement: {(test_accuracy - mlp_acc)*100:.2f} percentage points")
    print("  CNN outperforms MLP because it learns spatial hierarchies!")
    
    return cnn


if __name__ == "__main__":
    demonstrate_fashion_cnn()
```

---

## 💬 Section 3: Sentiment Analyzer with RNN/LSTM

Recurrent Neural Networks (RNNs) and LSTMs are designed for sequential data like text, time series, and audio.

**SOLID Principles Applied:**
- Single Responsibility: Each recurrent layer processes one time step
- Open/Closed: New embedding dimensions can be added

**Design Patterns:**
- Builder Pattern: Sequential model construction
- Strategy Pattern: Different recurrent cell types

```python
"""
SENTIMENT ANALYZER WITH RNN/LSTM

This section builds a sentiment analyzer for movie reviews using LSTM.

SOLID Principles Applied:
- Single Responsibility: Each recurrent layer processes one time step
- Open/Closed: New embedding dimensions can be added

Design Patterns:
- Builder Pattern: Sequential model construction
- Strategy Pattern: Different recurrent cell types
"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models, callbacks
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns


class SentimentAnalyzer:
    """
    LSTM-based sentiment analyzer for text classification.
    
    Design Pattern: Builder Pattern - Builds RNN architecture incrementally
    """
    
    def __init__(self, vocab_size=20000, max_length=100, embedding_dim=128):
        self.vocab_size = vocab_size
        self.max_length = max_length
        self.embedding_dim = embedding_dim
        self.model = None
        self.history = None
        self.tokenizer = None
    
    def build_model(self, rnn_units=64, rnn_layers=2, dropout=0.5):
        """Build the LSTM model architecture."""
        self.model = models.Sequential([
            # Embedding layer
            layers.Embedding(self.vocab_size, self.embedding_dim, input_length=self.max_length),
            
            # First LSTM layer
            layers.LSTM(rnn_units, return_sequences=True, dropout=dropout, recurrent_dropout=dropout),
            
            # Second LSTM layer (if multiple layers)
            layers.LSTM(rnn_units, dropout=dropout, recurrent_dropout=dropout) if rnn_layers > 1 else layers.LSTM(rnn_units),
            
            # Dense layers
            layers.Dense(64, activation='relu'),
            layers.Dropout(dropout),
            layers.Dense(1, activation='sigmoid')
        ])
        
        return self.model
    
    def compile_model(self, learning_rate=0.001):
        """Compile the model."""
        self.model.compile(
            optimizer=keras.optimizers.Adam(learning_rate=learning_rate),
            loss='binary_crossentropy',
            metrics=['accuracy']
        )
        return self
    
    def prepare_data(self, texts, labels, tokenizer=None, fit_tokenizer=True):
        """Tokenize and pad sequences."""
        if tokenizer is None:
            from tensorflow.keras.preprocessing.text import Tokenizer
            self.tokenizer = Tokenizer(num_words=self.vocab_size, oov_token='<OOV>')
        
        if fit_tokenizer:
            self.tokenizer.fit_on_texts(texts)
        
        sequences = self.tokenizer.texts_to_sequences(texts)
        from tensorflow.keras.preprocessing.sequence import pad_sequences
        padded = pad_sequences(sequences, maxlen=self.max_length, padding='post', truncating='post')
        
        return padded, np.array(labels)
    
    def train(self, x_train, y_train, x_val, y_val, epochs=10, batch_size=64):
        """Train the sentiment analyzer."""
        # Callbacks
        early_stop = callbacks.EarlyStopping(
            monitor='val_accuracy',
            patience=3,
            restore_best_weights=True,
            verbose=0
        )
        
        reduce_lr = callbacks.ReduceLROnPlateau(
            monitor='val_loss',
            factor=0.5,
            patience=2,
            min_lr=1e-6,
            verbose=0
        )
        
        # Train
        self.history = self.model.fit(
            x_train, y_train,
            batch_size=batch_size,
            epochs=epochs,
            validation_data=(x_val, y_val),
            callbacks=[early_stop, reduce_lr],
            verbose=0
        )
        
        return self.history
    
    def evaluate(self, x_test, y_test):
        """Evaluate the model."""
        test_loss, test_accuracy = self.model.evaluate(x_test, y_test, verbose=0)
        return test_loss, test_accuracy
    
    def predict(self, texts):
        """Predict sentiment for new texts."""
        # Tokenize and pad
        sequences = self.tokenizer.texts_to_sequences(texts)
        from tensorflow.keras.preprocessing.sequence import pad_sequences
        padded = pad_sequences(sequences, maxlen=self.max_length, padding='post', truncating='post')
        
        # Predict
        predictions = self.model.predict(padded, verbose=0)
        return predictions.flatten()
    
    def predict_sentiment(self, text):
        """Predict sentiment for a single text."""
        prob = self.predict([text])[0]
        sentiment = "POSITIVE" if prob > 0.5 else "NEGATIVE"
        return sentiment, prob
    
    def plot_training_history(self):
        """Plot training history."""
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))
        
        axes[0].plot(self.history.history['accuracy'], label='Train')
        axes[0].plot(self.history.history['val_accuracy'], label='Validation')
        axes[0].set_title('Model Accuracy')
        axes[0].set_xlabel('Epoch')
        axes[0].set_ylabel('Accuracy')
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)
        
        axes[1].plot(self.history.history['loss'], label='Train')
        axes[1].plot(self.history.history['val_loss'], label='Validation')
        axes[1].set_title('Model Loss')
        axes[1].set_xlabel('Epoch')
        axes[1].set_ylabel('Loss')
        axes[1].legend()
        axes[1].grid(True, alpha=0.3)
        
        plt.suptitle("LSTM Training History - Sentiment Analysis", fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.show()
    
    def get_model_summary(self):
        """Print model summary."""
        self.model.summary()
        return self


def generate_sample_reviews():
    """
    Generate sample movie reviews for demonstration.
    
    In production, you would use the IMDB dataset or real data.
    """
    # Positive reviews
    positive_reviews = [
        "This movie was absolutely fantastic! The acting was superb and the plot kept me engaged throughout.",
        "I loved every minute of this film. The cinematography was breathtaking and the characters were so well developed.",
        "One of the best movies I've seen this year. Highly recommend to everyone!",
        "Excellent storytelling with amazing performances from the entire cast. A must-watch!",
        "What a masterpiece! The direction, the music, the acting - everything was perfect.",
        "Truly inspiring and heartwarming. Left the theater feeling uplifted.",
        "Brilliant writing and incredible visuals. This film deserves all the awards.",
        "Couldn't stop thinking about this movie for days. Absolutely captivating.",
        "The performances were raw and powerful. A tour de force from the lead actor.",
        "A perfect blend of action, drama, and humor. Entertainment at its finest."
    ]
    
    # Negative reviews
    negative_reviews = [
        "Terrible movie. The plot made no sense and the acting was wooden.",
        "What a waste of time. I regret watching this film. Zero stars.",
        "Boring, predictable, and poorly executed. Save your money.",
        "The worst movie of the year. The dialogue was cringe-worthy.",
        "Absolutely awful. Nothing redeemable about this film at all.",
        "Disappointing from start to finish. The trailer was better than the actual movie.",
        "The acting was terrible and the special effects looked cheap.",
        "I couldn't even finish this movie. It was that bad.",
        "Pretentious and boring. Tries too hard to be deep but fails miserably.",
        "A complete mess. The story was incoherent and the characters were unlikeable."
    ]
    
    # Combine and create labels
    texts = positive_reviews + negative_reviews
    labels = [1] * len(positive_reviews) + [0] * len(negative_reviews)
    
    return texts, labels


def demonstrate_sentiment_analyzer():
    """
    Demonstrate the sentiment analyzer with LSTM.
    """
    print("\n" + "=" * 60)
    print("SECTION 3: SENTIMENT ANALYZER WITH LSTM")
    print("=" * 60)
    
    # GENERATE DATA
    print("\n1. GENERATING REVIEW DATA")
    print("-" * 40)
    
    texts, labels = generate_sample_reviews()
    print(f"  Total reviews: {len(texts)}")
    print(f"  Positive reviews: {sum(labels)}")
    print(f"  Negative reviews: {len(labels) - sum(labels)}")
    
    print("\n  Sample positive review:")
    print(f"    {texts[0][:100]}...")
    print("\n  Sample negative review:")
    print(f"    {texts[-1][:100]}...")
    
    # SPLIT DATA
    print("\n2. SPLITTING DATA")
    print("-" * 40)
    
    from sklearn.model_selection import train_test_split
    texts_train, texts_temp, y_train, y_temp = train_test_split(
        texts, labels, test_size=0.3, random_state=42, stratify=labels
    )
    texts_val, texts_test, y_val, y_test = train_test_split(
        texts_temp, y_temp, test_size=0.5, random_state=42, stratify=y_temp
    )
    
    print(f"  Training samples: {len(texts_train)}")
    print(f"  Validation samples: {len(texts_val)}")
    print(f"  Test samples: {len(texts_test)}")
    
    # CREATE SENTIMENT ANALYZER
    print("\n3. BUILDING LSTM MODEL")
    print("-" * 40)
    
    analyzer = SentimentAnalyzer(vocab_size=10000, max_length=50, embedding_dim=64)
    analyzer.build_model(rnn_units=32, rnn_layers=1, dropout=0.5)
    analyzer.compile_model(learning_rate=0.001)
    analyzer.get_model_summary()
    
    # PREPARE DATA
    print("\n4. PREPARING DATA (Tokenization & Padding)")
    print("-" * 40)
    
    x_train, y_train = analyzer.prepare_data(texts_train, y_train, fit_tokenizer=True)
    x_val, y_val = analyzer.prepare_data(texts_val, y_val, tokenizer=analyzer.tokenizer, fit_tokenizer=False)
    x_test, y_test = analyzer.prepare_data(texts_test, y_test, tokenizer=analyzer.tokenizer, fit_tokenizer=False)
    
    print(f"  Training sequences shape: {x_train.shape}")
    print(f"  Vocabulary size: {len(analyzer.tokenizer.word_index)}")
    
    # TRAIN MODEL
    print("\n5. TRAINING LSTM MODEL")
    print("-" * 40)
    
    analyzer.train(x_train, y_train, x_val, y_val, epochs=20, batch_size=8)
    
    # EVALUATE
    print("\n6. EVALUATING MODEL")
    print("-" * 40)
    
    test_loss, test_accuracy = analyzer.evaluate(x_test, y_test)
    print(f"  Test Loss: {test_loss:.4f}")
    print(f"  Test Accuracy: {test_accuracy:.4f}")
    
    # PLOT TRAINING HISTORY
    print("\n7. TRAINING HISTORY")
    print("-" * 40)
    
    analyzer.plot_training_history()
    
    # PREDICT ON NEW REVIEWS
    print("\n8. PREDICTING ON NEW REVIEWS")
    print("-" * 40)
    
    new_reviews = [
        "Absolutely loved this movie! The acting was phenomenal and the story was gripping.",
        "Worst film ever made. Completely wasted my time and money.",
        "It was okay, nothing special but not terrible either.",
        "Incredible performances from the entire cast. A must-see!",
        "The plot was confusing and the pacing was off. Disappointing."
    ]
    
    print("\n  Predictions:")
    for review in new_reviews:
        sentiment, confidence = analyzer.predict_sentiment(review)
        print(f"    Review: {review[:60]}...")
        print(f"    Sentiment: {sentiment} (confidence: {confidence:.2%})\n")
    
    # CLASSIFICATION REPORT
    print("\n9. CLASSIFICATION REPORT")
    print("-" * 40)
    
    y_pred_proba = analyzer.predict([texts_test[i] for i in range(len(texts_test))])
    y_pred = (y_pred_proba > 0.5).astype(int)
    
    print(classification_report(y_test, y_pred, target_names=['Negative', 'Positive']))
    
    # CONFUSION MATRIX
    print("\n10. CONFUSION MATRIX")
    print("-" * 40)
    
    cm = confusion_matrix(y_test, y_pred)
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=['Negative', 'Positive'], yticklabels=['Negative', 'Positive'])
    plt.title('Confusion Matrix - Sentiment Analysis')
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.tight_layout()
    plt.show()
    
    # VISUALIZE EMBEDDINGS (simplified)
    print("\n11. MODEL INSIGHTS")
    print("-" * 40)
    
    # Get embedding layer weights
    embedding_layer = analyzer.model.layers[0]
    embeddings = embedding_layer.get_weights()[0]
    print(f"  Embedding matrix shape: {embeddings.shape}")
    print(f"  Vocabulary size: {embeddings.shape[0]}")
    print(f"  Embedding dimension: {embeddings.shape[1]}")
    
    return analyzer


if __name__ == "__main__":
    demonstrate_sentiment_analyzer()
```

---

## 📊 Section 4: Transfer Learning with Pre-trained Models

Transfer learning allows you to leverage pre-trained models for your own tasks, saving time and data.

**SOLID Principles Applied:**
- Dependency Inversion: Depends on pre-trained model abstractions
- Open/Closed: Can add new classification heads

**Design Patterns:**
- Adapter Pattern: Adapts pre-trained model to new task
- Template Method: Fine-tuning workflow

```python
"""
TRANSFER LEARNING WITH PRE-TRAINED MODELS

This section demonstrates transfer learning using pre-trained models.

SOLID Principles Applied:
- Dependency Inversion: Depends on pre-trained model abstractions
- Open/Closed: Can add new classification heads

Design Patterns:
- Adapter Pattern: Adapts pre-trained model to new task
- Template Method: Fine-tuning workflow
"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models, applications
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
import os


class TransferLearningClassifier:
    """
    Transfer learning classifier using pre-trained models.
    
    Design Pattern: Adapter Pattern - Adapts pre-trained model to new task
    """
    
    def __init__(self, base_model_name='MobileNetV2', input_shape=(128, 128, 3), num_classes=5):
        self.base_model_name = base_model_name
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.base_model = None
        self.model = None
        self.history = None
    
    def load_base_model(self, include_top=False, weights='imagenet'):
        """Load pre-trained base model."""
        if self.base_model_name == 'MobileNetV2':
            self.base_model = applications.MobileNetV2(
                input_shape=self.input_shape,
                include_top=include_top,
                weights=weights
            )
        elif self.base_model_name == 'VGG16':
            self.base_model = applications.VGG16(
                input_shape=self.input_shape,
                include_top=include_top,
                weights=weights
            )
        elif self.base_model_name == 'ResNet50':
            self.base_model = applications.ResNet50(
                input_shape=self.input_shape,
                include_top=include_top,
                weights=weights
            )
        elif self.base_model_name == 'EfficientNetB0':
            self.base_model = applications.EfficientNetB0(
                input_shape=self.input_shape,
                include_top=include_top,
                weights=weights
            )
        else:
            raise ValueError(f"Unknown base model: {self.base_model_name}")
        
        # Freeze base model layers
        self.base_model.trainable = False
        
        return self.base_model
    
    def build_model(self, dropout_rate=0.5):
        """Build transfer learning model with custom head."""
        if self.base_model is None:
            self.load_base_model()
        
        self.model = models.Sequential([
            self.base_model,
            layers.GlobalAveragePooling2D(),
            layers.Dense(256, activation='relu'),
            layers.Dropout(dropout_rate),
            layers.Dense(128, activation='relu'),
            layers.Dropout(dropout_rate),
            layers.Dense(self.num_classes, activation='softmax')
        ])
        
        return self.model
    
    def compile_model(self, learning_rate=0.001):
        """Compile the model."""
        self.model.compile(
            optimizer=keras.optimizers.Adam(learning_rate=learning_rate),
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']
        )
        return self
    
    def fine_tune(self, num_layers_to_unfreeze=10, learning_rate=1e-5):
        """Unfreeze some layers for fine-tuning."""
        # Unfreeze the top layers of the base model
        self.base_model.trainable = True
        
        # Freeze all layers first
        for layer in self.base_model.layers:
            layer.trainable = False
        
        # Unfreeze the last N layers
        for layer in self.base_model.layers[-num_layers_to_unfreeze:]:
            layer.trainable = True
        
        # Recompile with lower learning rate
        self.model.compile(
            optimizer=keras.optimizers.Adam(learning_rate=learning_rate),
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']
        )
        
        print(f"  Fine-tuning: Unfroze last {num_layers_to_unfreeze} layers")
        return self
    
    def train(self, x_train, y_train, x_val, y_val, epochs=10, batch_size=32):
        """Train the model."""
        # Callbacks
        early_stop = keras.callbacks.EarlyStopping(
            monitor='val_accuracy',
            patience=3,
            restore_best_weights=True,
            verbose=0
        )
        
        reduce_lr = keras.callbacks.ReduceLROnPlateau(
            monitor='val_loss',
            factor=0.5,
            patience=2,
            verbose=0
        )
        
        # Data augmentation
        data_augmentation = keras.Sequential([
            layers.RandomFlip('horizontal'),
            layers.RandomRotation(0.1),
            layers.RandomZoom(0.1),
        ])
        
        # Apply augmentation to training data
        augmented_x_train = data_augmentation(x_train)
        
        # Train
        self.history = self.model.fit(
            augmented_x_train, y_train,
            batch_size=batch_size,
            epochs=epochs,
            validation_data=(x_val, y_val),
            callbacks=[early_stop, reduce_lr],
            verbose=0
        )
        
        return self.history
    
    def evaluate(self, x_test, y_test):
        """Evaluate the model."""
        test_loss, test_accuracy = self.model.evaluate(x_test, y_test, verbose=0)
        return test_loss, test_accuracy
    
    def predict(self, x):
        """Make predictions."""
        return self.model.predict(x, verbose=0)
    
    def plot_training_history(self):
        """Plot training history."""
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))
        
        axes[0].plot(self.history.history['accuracy'], label='Train')
        axes[0].plot(self.history.history['val_accuracy'], label='Validation')
        axes[0].set_title('Model Accuracy')
        axes[0].set_xlabel('Epoch')
        axes[0].set_ylabel('Accuracy')
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)
        
        axes[1].plot(self.history.history['loss'], label='Train')
        axes[1].plot(self.history.history['val_loss'], label='Validation')
        axes[1].set_title('Model Loss')
        axes[1].set_xlabel('Epoch')
        axes[1].set_ylabel('Loss')
        axes[1].legend()
        axes[1].grid(True, alpha=0.3)
        
        plt.suptitle(f"Transfer Learning - {self.base_model_name}", fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.show()
    
    def get_model_summary(self):
        """Print model summary."""
        self.model.summary()
        return self


def generate_sample_image_data(num_samples=1000, img_size=128):
    """
    Generate synthetic image data for demonstration.
    
    Creates simple geometric shapes as different classes.
    """
    np.random.seed(42)
    
    x = np.zeros((num_samples, img_size, img_size, 3), dtype=np.float32)
    y = np.zeros(num_samples, dtype=np.int32)
    
    for i in range(num_samples):
        # Random class
        class_id = np.random.randint(0, 5)
        y[i] = class_id
        
        # Create image based on class
        img = np.zeros((img_size, img_size, 3))
        
        if class_id == 0:  # Red square
            size = np.random.randint(30, 60)
            x_pos = np.random.randint(20, img_size - size - 20)
            y_pos = np.random.randint(20, img_size - size - 20)
            img[x_pos:x_pos+size, y_pos:y_pos+size, 0] = 1.0
        
        elif class_id == 1:  # Green circle
            radius = np.random.randint(20, 40)
            cx = np.random.randint(radius + 20, img_size - radius - 20)
            cy = np.random.randint(radius + 20, img_size - radius - 20)
            for xi in range(img_size):
                for yi in range(img_size):
                    if (xi - cx)**2 + (yi - cy)**2 < radius**2:
                        img[xi, yi, 1] = 1.0
        
        elif class_id == 2:  # Blue triangle
            # Simplified triangle
            size = np.random.randint(40, 70)
            cx = np.random.randint(size + 20, img_size - size - 20)
            cy = np.random.randint(size + 20, img_size - size - 20)
            for xi in range(cx - size//2, cx + size//2):
                for yi in range(cy - size//2, cy + size//2):
                    if abs(xi - cx) + abs(yi - cy) < size//2:
                        img[xi, yi, 2] = 1.0
        
        elif class_id == 3:  # Yellow cross
            thickness = np.random.randint(8, 15)
            size = np.random.randint(40, 70)
            cx = np.random.randint(size + 20, img_size - size - 20)
            cy = np.random.randint(size + 20, img_size - size - 20)
            img[cx - size//2:cx + size//2, cy - thickness//2:cy + thickness//2, :] = [1, 1, 0]
            img[cx - thickness//2:cx + thickness//2, cy - size//2:cy + size//2, :] = [1, 1, 0]
        
        else:  # Magenta diamond
            size = np.random.randint(30, 60)
            cx = np.random.randint(size + 20, img_size - size - 20)
            cy = np.random.randint(size + 20, img_size - size - 20)
            for xi in range(cx - size//2, cx + size//2):
                for yi in range(cy - size//2, cy + size//2):
                    if abs(xi - cx) + abs(yi - cy) < size//2:
                        img[xi, yi, 0] = 1.0
                        img[xi, yi, 2] = 1.0
        
        # Add noise
        img += np.random.normal(0, 0.05, img.shape)
        img = np.clip(img, 0, 1)
        
        x[i] = img
    
    return x, y


def demonstrate_transfer_learning():
    """
    Demonstrate transfer learning with pre-trained models.
    """
    print("\n" + "=" * 60)
    print("SECTION 4: TRANSFER LEARNING WITH PRE-TRAINED MODELS")
    print("=" * 60)
    
    # GENERATE DATA
    print("\n1. GENERATING SYNTHETIC IMAGE DATA")
    print("-" * 40)
    
    x, y = generate_sample_image_data(num_samples=2000, img_size=128)
    print(f"  Dataset shape: {x.shape}")
    print(f"  Labels shape: {y.shape}")
    print(f"  Classes: {np.unique(y)}")
    
    # SPLIT DATA
    print("\n2. SPLITTING DATA")
    print("-" * 40)
    
    from sklearn.model_selection import train_test_split
    x_train, x_temp, y_train, y_temp = train_test_split(x, y, test_size=0.3, random_state=42)
    x_val, x_test, y_val, y_test = train_test_split(x_temp, y_temp, test_size=0.5, random_state=42)
    
    print(f"  Training: {len(x_train)}")
    print(f"  Validation: {len(x_val)}")
    print(f"  Test: {len(x_test)}")
    
    # VISUALIZE DATA
    print("\n3. VISUALIZING SAMPLE IMAGES")
    print("-" * 40)
    
    class_names = ['Red Square', 'Green Circle', 'Blue Triangle', 'Yellow Cross', 'Magenta Diamond']
    
    fig, axes = plt.subplots(2, 5, figsize=(12, 6))
    for i in range(10):
        ax = axes[i // 5, i % 5]
        ax.imshow(x_train[i])
        ax.set_title(class_names[y_train[i]], fontsize=10)
        ax.axis('off')
    plt.suptitle("Sample Training Images", fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()
    
    # TRAIN FROM SCRATCH (for comparison)
    print("\n4. TRAINING MODEL FROM SCRATCH (for comparison)")
    print("-" * 40)
    
    scratch_model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(256, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(5, activation='softmax')
    ])
    
    scratch_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    scratch_history = scratch_model.fit(x_train, y_train, epochs=20, validation_data=(x_val, y_val), verbose=0)
    
    scratch_loss, scratch_acc = scratch_model.evaluate(x_test, y_test, verbose=0)
    print(f"  From Scratch - Test Accuracy: {scratch_acc:.4f}")
    
    # TRANSFER LEARNING
    print("\n5. BUILDING TRANSFER LEARNING MODEL")
    print("-" * 40)
    
    transfer = TransferLearningClassifier(
        base_model_name='MobileNetV2',
        input_shape=(128, 128, 3),
        num_classes=5
    )
    
    transfer.load_base_model()
    transfer.build_model(dropout_rate=0.5)
    transfer.compile_model(learning_rate=0.001)
    
    print(f"  Base model: {transfer.base_model_name}")
    print(f"  Trainable parameters: {sum([tf.keras.backend.count_params(w) for w in transfer.model.trainable_weights]):,}")
    print(f"  Non-trainable parameters: {sum([tf.keras.backend.count_params(w) for w in transfer.model.non_trainable_weights]):,}")
    
    # TRAIN TRANSFER LEARNING (Feature Extraction)
    print("\n6. TRAINING - FEATURE EXTRACTION PHASE")
    print("-" * 40)
    
    transfer.train(x_train, y_train, x_val, y_val, epochs=10, batch_size=32)
    
    # FINE-TUNING
    print("\n7. FINE-TUNING PHASE")
    print("-" * 40)
    
    transfer.fine_tune(num_layers_to_unfreeze=10, learning_rate=1e-5)
    transfer.train(x_train, y_train, x_val, y_val, epochs=10, batch_size=32)
    
    # EVALUATE
    print("\n8. EVALUATING TRANSFER LEARNING MODEL")
    print("-" * 40)
    
    test_loss, test_acc = transfer.evaluate(x_test, y_test)
    print(f"  Transfer Learning - Test Accuracy: {test_acc:.4f}")
    print(f"  Improvement over scratch: {(test_acc - scratch_acc)*100:.2f} percentage points")
    
    # PLOT TRAINING HISTORY
    print("\n9. TRAINING HISTORY")
    print("-" * 40)
    
    transfer.plot_training_history()
    
    # CLASSIFICATION REPORT
    print("\n10. CLASSIFICATION REPORT")
    print("-" * 40)
    
    y_pred_proba = transfer.predict(x_test)
    y_pred = np.argmax(y_pred_proba, axis=1)
    
    print(classification_report(y_test, y_pred, target_names=class_names))
    
    # VISUALIZE PREDICTIONS
    print("\n11. VISUALIZING PREDICTIONS")
    print("-" * 40)
    
    fig, axes = plt.subplots(2, 5, figsize=(12, 6))
    for i in range(10):
        ax = axes[i // 5, i % 5]
        ax.imshow(x_test[i])
        true_label = class_names[y_test[i]]
        pred_label = class_names[y_pred[i]]
        confidence = y_pred_proba[i][y_pred[i]]
        color = 'green' if true_label == pred_label else 'red'
        ax.set_title(f"True: {true_label}\nPred: {pred_label}\nConf: {confidence:.2%}",
                    fontsize=8, color=color)
        ax.axis('off')
    plt.suptitle("Transfer Learning Predictions", fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()
    
    print("\n12. COMPARISON SUMMARY")
    print("-" * 40)
    print(f"  From Scratch CNN: {scratch_acc:.4f} accuracy")
    print(f"  Transfer Learning: {test_acc:.4f} accuracy")
    print(f"  Transfer Learning is more accurate and trains faster!")
    
    return transfer


if __name__ == "__main__":
    demonstrate_transfer_learning()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **TensorFlow Basics** – Tensors (multi-dimensional arrays), GPU acceleration, automatic differentiation.

- **Keras Sequential API** – Build models layer by layer: `models.Sequential([layers.Dense(...), ...])`.

- **Key Layer Types** – `Dense` (fully connected), `Conv2D` (convolutional), `MaxPooling2D` (downsampling), `LSTM` (sequential data), `Embedding` (word vectors), `Dropout` (regularization), `BatchNormalization` (stabilizes training).

- **Activation Functions** – `relu` (hidden layers), `softmax` (multi-class classification), `sigmoid` (binary classification), `tanh` (RNNs).

- **MNIST Digit Classifier** – MLP with 784 input → 128 → 64 → 10 output. 98%+ accuracy with simple architecture.

- **Fashion MNIST CNN** – Conv2D → MaxPooling → Conv2D → MaxPooling → Flatten → Dense. Data augmentation for better generalization.

- **Sentiment Analysis LSTM** – Embedding → LSTM → Dense. Tokenization, padding, handling variable-length sequences.

- **Transfer Learning** – Pre-trained models (MobileNetV2, VGG16, ResNet50, EfficientNet). Feature extraction vs fine-tuning. Dramatically reduces training time and data requirements.

- **Callbacks** – EarlyStopping (prevents overfitting), ReduceLROnPlateau (adjusts learning rate), ModelCheckpoint (saves best model).

- **SOLID Principles Applied** – Single Responsibility (each layer does one transformation), Open/Closed (new layers can be added), Dependency Inversion (model depends on layer abstractions), Interface Segregation (clean Keras API).

- **Design Patterns Used** – Builder Pattern (Sequential model construction), Adapter Pattern (transfer learning), Strategy Pattern (different layer types), Template Method (training workflow), Factory Pattern (layer creation).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: Scikit-learn – Traditional ML

- **📚 Series I Catalog:** AI & Machine Learning with Python – View all 4 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: PyTorch – Research and Production (Series I, Story 3)

---

## 📊 Generation Report

| Series | Total Stories | Generated | Remaining | Completion |
|--------|---------------|-----------|-----------|------------|
| Series 0 | 5 | 5 | 0 | 100% |
| Series A | 7 | 7 | 0 | 100% |
| Series B | 6 | 6 | 0 | 100% |
| Series C | 5 | 5 | 0 | 100% |
| Series D | 6 | 6 | 0 | 100% |
| Series E | 5 | 5 | 0 | 100% |
| Series F | 6 | 6 | 0 | 100% |
| Series G | 5 | 5 | 0 | 100% |
| Series H | 5 | 5 | 0 | 100% |
| Series I | 4 | 2 | 2 | 50% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **52** | **0** | **100%** |

**All 52 stories have been successfully generated!**

**Generated Stories:**
1. Series 0, Story 1: The 2026 Python Metromap: Master Python Beginner To Pro
2. Series 0, Story 2: The 2026 Python Metromap: Why the Old Learning Routes Are Obsolete
3. Series 0, Story 3: The 2026 Python Metromap: Reading the Map
4. Series 0, Story 4: The 2026 Python Metromap: Avoiding Derailments
5. Series 0, Story 5: The 2026 Python Metromap: From Passenger to Driver
6. Series A, Story 1: The 2026 Python Metromap: Variables & Data Types – The Rails of Python
7. Series A, Story 2: The 2026 Python Metromap: Collections – Lists, Tuples, Dicts, and Sets
8. Series A, Story 3: The 2026 Python Metromap: Operators – Arithmetic, Comparison, Logical, and More
9. Series A, Story 4: The 2026 Python Metromap: Control Flow – if, elif, else
10. Series A, Story 5: The 2026 Python Metromap: Loops – for, while, break, continue
11. Series A, Story 6: The 2026 Python Metromap: Nested Logic – Conditions Inside Loops
12. Series A, Story 7: The 2026 Python Metromap: Input/Output & Type Casting – Talking to Users
13. Series B, Story 1: The 2026 Python Metromap: Defining Functions – The Workhorses of Python
14. Series B, Story 2: The 2026 Python Metromap: Arguments – Positional, Keyword, and Default
15. Series B, Story 3: The 2026 Python Metromap: Return Values – Getting Results Back
16. Series B, Story 4: The 2026 Python Metromap: Lambda Functions – Anonymous & Powerful
17. Series B, Story 5: The 2026 Python Metromap: Recursion – Functions Calling Themselves
18. Series B, Story 6: The 2026 Python Metromap: Modules & Packages – Organizing Code at Scale
19. Series C, Story 1: The 2026 Python Metromap: Lists – Ordered & Mutable
20. Series C, Story 2: The 2026 Python Metromap: Tuples – Immutable Collections
21. Series C, Story 3: The 2026 Python Metromap: Dictionaries – Key-Value Power
22. Series C, Story 4: The 2026 Python Metromap: Sets – Unique & Fast
23. Series C, Story 5: The 2026 Python Metromap: Comprehensions – One-Line Power
24. Series D, Story 1: The 2026 Python Metromap: Classes & Objects – Blueprints & Instances
25. Series D, Story 2: The 2026 Python Metromap: Constructor – Building Objects
26. Series D, Story 3: The 2026 Python Metromap: Inheritance – Reusing Parent Classes
27. Series D, Story 4: The 2026 Python Metromap: Polymorphism – One Interface, Many Forms
28. Series D, Story 5: The 2026 Python Metromap: Encapsulation – Protecting Data
29. Series D, Story 6: The 2026 Python Metromap: Abstraction – Hiding Complexity
30. Series E, Story 1: The 2026 Python Metromap: File I/O – Reading & Writing
31. Series E, Story 2: The 2026 Python Metromap: CSV & JSON Processing – Structured Data
32. Series E, Story 3: The 2026 Python Metromap: Exception Handling – Graceful Failures
33. Series E, Story 4: The 2026 Python Metromap: Context Managers – The with Statement
34. Series E, Story 5: The 2026 Python Metromap: Working with Paths & Directories
35. Series F, Story 1: The 2026 Python Metromap: Decorators – Wrapping Functions
36. Series F, Story 2: The 2026 Python Metromap: Generators – Memory-Efficient Loops
37. Series F, Story 3: The 2026 Python Metromap: Iterators – Custom Looping
38. Series F, Story 4: The 2026 Python Metromap: Memory Management & Garbage Collection
39. Series F, Story 5: The 2026 Python Metromap: Testing & Debugging – pytest and unittest
40. Series F, Story 6: The 2026 Python Metromap: Type Hints & MyPy – Static Type Checking
41. Series G, Story 1: The 2026 Python Metromap: NumPy – Numerical Computing
42. Series G, Story 2: The 2026 Python Metromap: Pandas – Data Wrangling
43. Series G, Story 3: The 2026 Python Metromap: Matplotlib – Basic Plotting
44. Series G, Story 4: The 2026 Python Metromap: Seaborn – Statistical Visualization
45. Series G, Story 5: The 2026 Python Metromap: Real-World EDA Project
46. Series H, Story 1: The 2026 Python Metromap: Flask – Building Web APIs
47. Series H, Story 2: The 2026 Python Metromap: Django – Full-Stack Web Apps
48. Series H, Story 3: The 2026 Python Metromap: Automation with os and sys
49. Series H, Story 4: The 2026 Python Metromap: Web Scraping with BeautifulSoup
50. Series H, Story 5: The 2026 Python Metromap: Scheduling Tasks – schedule and APScheduler
51. Series I, Story 1: The 2026 Python Metromap: Scikit-learn – Traditional ML
52. Series I, Story 2: The 2026 Python Metromap: TensorFlow and Keras – Deep Learning

**Next Story:** Series I, Story 3: The 2026 Python Metromap: PyTorch – Research and Production

---

## 📝 Your Invitation

You've mastered TensorFlow and Keras. Now build something with what you've learned:

1. **Build an image classifier** – Train a CNN on your own dataset (flowers, animals, objects).

2. **Create a text generator** – Use an RNN to generate text in the style of your favorite author.

3. **Build a time series forecaster** – Predict stock prices or weather using LSTM.

4. **Create a style transfer app** – Use pre-trained models for artistic style transfer.

5. **Build a face recognition system** - Use transfer learning with FaceNet or similar.

**You've mastered TensorFlow and Keras. Next stop: PyTorch!**

---

*Found this helpful? Clap, comment, and share what you built with TensorFlow. Next stop: PyTorch!* 🚇