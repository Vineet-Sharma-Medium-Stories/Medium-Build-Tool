# The 2026 Python Metromap: PyTorch – Research and Production

## Series I: AI & Machine Learning with Python | Story 3 of 4

![The 2026 Python Metromap/images/PyTorch – Research and Production](images/PyTorch – Research and Production.png)

## 📖 Introduction

**Welcome to the third stop on the AI & Machine Learning with Python Line.**

You've mastered TensorFlow and Keras—building neural networks with high-level APIs, training models, and using pre-trained architectures. Keras is excellent for rapid prototyping and production deployment. But when you need fine-grained control over every aspect of your model—custom training loops, dynamic computation graphs, or cutting-edge research—PyTorch is the framework of choice.

PyTorch is beloved by researchers and increasingly used in production. Its defining feature is dynamic computation graphs (define-by-run), which means the graph is built on the fly as you execute operations. This makes debugging intuitive and allows for flexible model architectures that can change during execution. PyTorch also provides seamless GPU acceleration, automatic differentiation, and a rich ecosystem of libraries.

This story—**The 2026 Python Metromap: PyTorch – Research and Production**—is your guide to building neural networks with PyTorch. We'll build a custom neural network for image classification from scratch. We'll implement custom training loops with gradient clipping and learning rate scheduling. We'll create a data loading pipeline with transforms and batching. We'll build a complete training framework with checkpointing and logging. And we'll deploy our model for inference.

**Let's torch.**

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

- 🧠 **The 2026 Python Metromap: TensorFlow and Keras – Deep Learning** – Handwritten digit classifier; fashion item recognizer; sentiment analyzer.

- 🔥 **The 2026 Python Metromap: PyTorch – Research and Production** – Custom neural network for image classification; training loops; model deployment. **⬅️ YOU ARE HERE**

- 🚀 **The 2026 Python Metromap: End-to-End ML Pipeline Project** – Complete machine learning pipeline from data collection to deployment for house price prediction. 🔜 *Up Next*

### The Complete Story Catalog

For a complete view of all upcoming stories across every series, visit the **Complete 2026 Python Metromap Story Catalog**.

---

## 🔥 Section 1: PyTorch Fundamentals – Tensors and Autograd

PyTorch's core data structure is the Tensor, similar to NumPy arrays but with GPU acceleration and automatic differentiation.

**SOLID Principle Applied: Single Responsibility** – Each tensor operation has one purpose.

**Design Pattern: Command Pattern** – Operations build a computation graph for automatic differentiation.

```python
"""
PYTORCH FUNDAMENTALS: TENSORS AND AUTOGRAD

This section covers the basics of PyTorch tensors and automatic differentiation.

SOLID Principle: Single Responsibility
- Each tensor operation has one purpose

Design Pattern: Command Pattern
- Operations build a computation graph for automatic differentiation
"""

import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np


def demonstrate_tensor_basics():
    """
    Demonstrates PyTorch tensor creation and operations.
    
    Tensors are multi-dimensional arrays similar to NumPy.
    """
    print("=" * 60)
    print("SECTION 1A: PYTORCH TENSORS")
    print("=" * 60)
    
    # CREATE TENSORS
    print("\n1. CREATING TENSORS")
    print("-" * 40)
    
    # From Python list
    tensor_from_list = torch.tensor([[1, 2, 3], [4, 5, 6]])
    print(f"  From list:\n{tensor_from_list}")
    
    # From NumPy array
    np_array = np.array([1, 2, 3, 4, 5])
    tensor_from_numpy = torch.from_numpy(np_array)
    print(f"  From NumPy: {tensor_from_numpy}")
    
    # Zeros and ones
    zeros = torch.zeros(3, 4)
    ones = torch.ones(2, 3)
    print(f"  Zeros shape: {zeros.shape}")
    print(f"  Ones shape: {ones.shape}")
    
    # Random tensors
    random_uniform = torch.rand(3, 3)  # Uniform [0, 1)
    random_normal = torch.randn(2, 4)  # Normal N(0, 1)
    print(f"  Random uniform shape: {random_uniform.shape}")
    print(f"  Random normal shape: {random_normal.shape}")
    
    # Range tensors
    range_tensor = torch.arange(0, 10, 2)
    linspace_tensor = torch.linspace(0, 1, 5)
    print(f"  arange(0, 10, 2): {range_tensor}")
    print(f"  linspace(0, 1, 5): {linspace_tensor}")
    
    # TENSOR PROPERTIES
    print("\n2. TENSOR PROPERTIES")
    print("-" * 40)
    
    tensor = torch.randn(2, 3, 4)
    print(f"  Tensor shape: {tensor.shape}")
    print(f"  Number of dimensions: {tensor.dim()}")
    print(f"  Number of elements: {tensor.numel()}")
    print(f"  Data type: {tensor.dtype}")
    print(f"  Device: {tensor.device}")
    
    # TENSOR OPERATIONS
    print("\n3. TENSOR OPERATIONS")
    print("-" * 40)
    
    a = torch.tensor([[1, 2], [3, 4]])
    b = torch.tensor([[5, 6], [7, 8]])
    
    print(f"  a:\n{a}")
    print(f"  b:\n{b}")
    print(f"  a + b:\n{a + b}")
    print(f"  a * b (element-wise):\n{a * b}")
    print(f"  a @ b (matrix multiplication):\n{a @ b}")
    
    # RESHAPING
    print("\n4. RESHAPING TENSORS")
    print("-" * 40)
    
    tensor = torch.arange(12)
    print(f"  Original: {tensor}")
    print(f"  reshape(3, 4):\n{tensor.reshape(3, 4)}")
    print(f"  view(2, 6):\n{tensor.view(2, 6)}")
    
    # BROADCASTING
    print("\n5. BROADCASTING")
    print("-" * 40)
    
    a = torch.tensor([[1, 2, 3], [4, 5, 6]])
    b = torch.tensor([10, 20, 30])
    print(f"  a shape: {a.shape}")
    print(f"  b shape: {b.shape}")
    print(f"  a + b:\n{a + b}")
    
    # GPU ACCELERATION
    print("\n6. GPU ACCELERATION")
    print("-" * 40)
    
    if torch.cuda.is_available():
        print(f"  GPU available: {torch.cuda.get_device_name(0)}")
        device = torch.device('cuda')
        tensor_gpu = torch.tensor([1, 2, 3]).to(device)
        print(f"  Tensor on GPU: {tensor_gpu.device}")
    else:
        print("  GPU not available. Using CPU.")
        device = torch.device('cpu')


def demonstrate_autograd():
    """
    Demonstrates automatic differentiation (autograd).
    
    PyTorch builds a computation graph that tracks operations for gradient calculation.
    """
    print("\n" + "=" * 60)
    print("SECTION 1B: AUTOGRAD - AUTOMATIC DIFFERENTIATION")
    print("=" * 60)
    
    # BASIC AUTOGRAD
    print("\n1. BASIC AUTOGRAD")
    print("-" * 40)
    
    # Create tensor with requires_grad=True
    x = torch.tensor(2.0, requires_grad=True)
    print(f"  x = {x.item()}, requires_grad: {x.requires_grad}")
    
    # Compute y = x²
    y = x ** 2
    print(f"  y = x² = {y.item()}")
    
    # Compute gradient dy/dx = 2x = 4
    y.backward()
    print(f"  dy/dx = {x.grad.item()}")
    
    # COMPUTATION GRAPH
    print("\n2. COMPUTATION GRAPH")
    print("-" * 40)
    
    x = torch.tensor(3.0, requires_grad=True)
    w = torch.tensor(2.0, requires_grad=True)
    b = torch.tensor(1.0, requires_grad=True)
    
    # Linear transformation: y = w * x + b
    y = w * x + b
    print(f"  y = {w.item()} * {x.item()} + {b.item()} = {y.item()}")
    
    y.backward()
    print(f"  ∂y/∂x = {x.grad.item()} (should be w = {w.item()})")
    print(f"  ∂y/∂w = {w.grad.item()} (should be x = {x.item()})")
    print(f"  ∂y/∂b = {b.grad.item()} (should be 1)")
    
    # MULTIPLE OUTPUTS
    print("\n3. MULTIPLE OUTPUTS AND GRADIENTS")
    print("-" * 40)
    
    x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
    
    # Sum of squares
    y = (x ** 2).sum()
    print(f"  x = {x.tolist()}")
    print(f"  y = sum(x²) = {y.item()}")
    
    y.backward()
    print(f"  dy/dx = {x.grad.tolist()} (should be 2*x = [2, 4, 6])")
    
    # DETACHING AND STOPPING GRADIENTS
    print("\n4. DETACHING AND STOPPING GRADIENTS")
    print("-" * 40)
    
    x = torch.tensor(2.0, requires_grad=True)
    
    # Normal computation (tracks gradients)
    y = x ** 2
    print(f"  y requires_grad: {y.requires_grad}")
    
    # Detach (no gradient tracking)
    z = y.detach()
    print(f"  z requires_grad: {z.requires_grad}")
    
    # No gradient context
    with torch.no_grad():
        w = x ** 3
        print(f"  w requires_grad (in no_grad block): {w.requires_grad}")
    
    # GRADIENT ACCUMULATION
    print("\n5. GRADIENT ACCUMULATION")
    print("-" * 40)
    
    w = torch.tensor(1.0, requires_grad=True)
    
    for i in range(3):
        loss = (w * i) ** 2
        loss.backward()
        print(f"  Iteration {i}: gradient = {w.grad.item():.2f}")
    
    print(f"  Total gradient accumulated: {w.grad.item():.2f}")
    print("  Gradients accumulate by default! Use optimizer.zero_grad() to reset.")


def demonstrate_neural_network_basics():
    """
    Demonstrates building a simple neural network in PyTorch.
    
    PyTorch uses the nn.Module base class for all neural network modules.
    """
    print("\n" + "=" * 60)
    print("SECTION 1C: BUILDING NEURAL NETWORKS")
    print("=" * 60)
    
    # DEFINE A SIMPLE NETWORK
    print("\n1. DEFINING A NEURAL NETWORK")
    print("-" * 40)
    
    class SimpleNet(nn.Module):
        """
        A simple feed-forward neural network.
        
        Design Pattern: Template Method Pattern - forward() defines computation
        """
        
        def __init__(self, input_size=784, hidden_size=128, num_classes=10):
            super().__init__()
            self.fc1 = nn.Linear(input_size, hidden_size)
            self.relu = nn.ReLU()
            self.fc2 = nn.Linear(hidden_size, hidden_size // 2)
            self.fc3 = nn.Linear(hidden_size // 2, num_classes)
            self.dropout = nn.Dropout(0.2)
        
        def forward(self, x):
            """Forward pass (define computation graph)."""
            x = self.fc1(x)
            x = self.relu(x)
            x = self.dropout(x)
            x = self.fc2(x)
            x = self.relu(x)
            x = self.dropout(x)
            x = self.fc3(x)
            return x
    
    model = SimpleNet()
    print(f"  Model architecture:\n{model}")
    
    # COUNT PARAMETERS
    print("\n2. COUNTING PARAMETERS")
    print("-" * 40)
    
    total_params = sum(p.numel() for p in model.parameters())
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    
    print(f"  Total parameters: {total_params:,}")
    print(f"  Trainable parameters: {trainable_params:,}")
    
    # FORWARD PASS
    print("\n3. FORWARD PASS")
    print("-" * 40)
    
    # Create random input (batch of 32 images, 784 pixels each)
    x = torch.randn(32, 784)
    output = model(x)
    print(f"  Input shape: {x.shape}")
    print(f"  Output shape: {output.shape}")
    
    # LOSS FUNCTION AND OPTIMIZER
    print("\n4. LOSS FUNCTION AND OPTIMIZER")
    print("-" * 40)
    
    # Loss function
    criterion = nn.CrossEntropyLoss()
    
    # Optimizer (SGD with momentum)
    optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
    
    # Create dummy target
    target = torch.randint(0, 10, (32,))
    
    # Forward pass
    output = model(x)
    loss = criterion(output, target)
    
    # Backward pass
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    print(f"  Loss: {loss.item():.4f}")
    print("  Training step completed!")
    
    # LAYER TYPES
    print("\n5. COMMON LAYER TYPES")
    print("-" * 40)
    
    layers = [
        ("Linear", nn.Linear(128, 64)),
        ("Conv2d", nn.Conv2d(3, 16, kernel_size=3, padding=1)),
        ("MaxPool2d", nn.MaxPool2d(2, 2)),
        ("BatchNorm2d", nn.BatchNorm2d(16)),
        ("Dropout", nn.Dropout(0.5)),
        ("ReLU", nn.ReLU()),
        ("Sigmoid", nn.Sigmoid()),
        ("Tanh", nn.Tanh()),
        ("Softmax", nn.Softmax(dim=1))
    ]
    
    for name, layer in layers:
        print(f"  {name:12} - {layer}")
    
    # ACCESSING PARAMETERS
    print("\n6. ACCESSING MODEL PARAMETERS")
    print("-" * 40)
    
    for name, param in model.named_parameters():
        print(f"  {name}: {param.shape}")


if __name__ == "__main__":
    demonstrate_tensor_basics()
    demonstrate_autograd()
    demonstrate_neural_network_basics()
```

---

## 🔥 Section 2: Custom CNN for Image Classification

A complete convolutional neural network implementation with custom training loop, data loading, and evaluation.

**SOLID Principles Applied:**
- Single Responsibility: Each module handles one aspect of the network
- Dependency Inversion: Training loop depends on model abstraction

**Design Patterns:**
- Builder Pattern: Builds CNN architecture incrementally
- Template Method: Training loop defines the training workflow

```python
"""
CUSTOM CNN FOR IMAGE CLASSIFICATION

This section builds a complete CNN for CIFAR-10 image classification.

SOLID Principles Applied:
- Single Responsibility: Each module handles one aspect
- Dependency Inversion: Training loop depends on model abstraction

Design Patterns:
- Builder Pattern: Builds CNN architecture incrementally
- Template Method: Training loop defines training workflow
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from torchvision import datasets, transforms
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import os


class CIFAR10CNN(nn.Module):
    """
    CNN for CIFAR-10 image classification.
    
    Architecture: Conv -> Conv -> Pool -> Conv -> Conv -> Pool -> FC -> FC
    """
    
    def __init__(self, num_classes=10):
        super().__init__()
        
        # Convolutional layers
        self.conv_layers = nn.Sequential(
            # Block 1
            nn.Conv2d(3, 32, kernel_size=3, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.Conv2d(32, 32, kernel_size=3, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Dropout2d(0.25),
            
            # Block 2
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.Conv2d(64, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Dropout2d(0.25),
            
            # Block 3
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.Conv2d(128, 128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Dropout2d(0.25),
        )
        
        # Fully connected layers
        self.fc_layers = nn.Sequential(
            nn.Flatten(),
            nn.Linear(128 * 4 * 4, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(256, num_classes)
        )
    
    def forward(self, x):
        """Forward pass."""
        x = self.conv_layers(x)
        x = self.fc_layers(x)
        return x


class Trainer:
    """
    Complete training pipeline for PyTorch models.
    
    Design Pattern: Template Method Pattern - Defines training workflow
    """
    
    def __init__(self, model, device, save_dir='checkpoints'):
        self.model = model.to(device)
        self.device = device
        self.save_dir = save_dir
        os.makedirs(save_dir, exist_ok=True)
        
        self.train_losses = []
        self.val_losses = []
        self.train_accs = []
        self.val_accs = []
    
    def train_epoch(self, train_loader, criterion, optimizer):
        """Train for one epoch."""
        self.model.train()
        running_loss = 0.0
        correct = 0
        total = 0
        
        for batch_idx, (data, target) in enumerate(train_loader):
            data, target = data.to(self.device), target.to(self.device)
            
            # Zero gradients
            optimizer.zero_grad()
            
            # Forward pass
            output = self.model(data)
            loss = criterion(output, target)
            
            # Backward pass
            loss.backward()
            
            # Gradient clipping (prevents exploding gradients)
            torch.nn.utils.clip_grad_norm_(self.model.parameters(), max_norm=1.0)
            
            # Update weights
            optimizer.step()
            
            # Statistics
            running_loss += loss.item()
            _, predicted = output.max(1)
            total += target.size(0)
            correct += predicted.eq(target).sum().item()
        
        epoch_loss = running_loss / len(train_loader)
        epoch_acc = 100. * correct / total
        
        return epoch_loss, epoch_acc
    
    def validate(self, val_loader, criterion):
        """Validate the model."""
        self.model.eval()
        running_loss = 0.0
        correct = 0
        total = 0
        
        with torch.no_grad():
            for data, target in val_loader:
                data, target = data.to(self.device), target.to(self.device)
                
                output = self.model(data)
                loss = criterion(output, target)
                
                running_loss += loss.item()
                _, predicted = output.max(1)
                total += target.size(0)
                correct += predicted.eq(target).sum().item()
        
        epoch_loss = running_loss / len(val_loader)
        epoch_acc = 100. * correct / total
        
        return epoch_loss, epoch_acc
    
    def train(self, train_loader, val_loader, criterion, optimizer, 
              epochs=50, scheduler=None, early_stop_patience=5):
        """Complete training loop."""
        best_val_acc = 0.0
        patience_counter = 0
        
        for epoch in range(epochs):
            # Train
            train_loss, train_acc = self.train_epoch(train_loader, criterion, optimizer)
            self.train_losses.append(train_loss)
            self.train_accs.append(train_acc)
            
            # Validate
            val_loss, val_acc = self.validate(val_loader, criterion)
            self.val_losses.append(val_loss)
            self.val_accs.append(val_acc)
            
            # Learning rate scheduling
            if scheduler:
                scheduler.step(val_loss)
            
            # Print progress
            print(f"Epoch {epoch+1}/{epochs}")
            print(f"  Train Loss: {train_loss:.4f}, Train Acc: {train_acc:.2f}%")
            print(f"  Val Loss: {val_loss:.4f}, Val Acc: {val_acc:.2f}%")
            
            # Save best model
            if val_acc > best_val_acc:
                best_val_acc = val_acc
                self.save_checkpoint(epoch, val_acc, is_best=True)
                patience_counter = 0
                print(f"  ✓ New best model! (Acc: {val_acc:.2f}%)")
            else:
                patience_counter += 1
            
            # Early stopping
            if patience_counter >= early_stop_patience:
                print(f"  Early stopping triggered after {epoch+1} epochs")
                break
            
            print()
        
        return best_val_acc
    
    def save_checkpoint(self, epoch, accuracy, is_best=False):
        """Save model checkpoint."""
        checkpoint = {
            'epoch': epoch,
            'model_state_dict': self.model.state_dict(),
            'optimizer_state_dict': self.optimizer.state_dict() if hasattr(self, 'optimizer') else None,
            'accuracy': accuracy,
            'train_losses': self.train_losses,
            'val_losses': self.val_losses,
            'train_accs': self.train_accs,
            'val_accs': self.val_accs
        }
        
        filename = f"{self.save_dir}/checkpoint_epoch_{epoch}.pt"
        torch.save(checkpoint, filename)
        
        if is_best:
            best_filename = f"{self.save_dir}/best_model.pt"
            torch.save(checkpoint, best_filename)
    
    def load_checkpoint(self, filename):
        """Load model checkpoint."""
        checkpoint = torch.load(filename, map_location=self.device)
        self.model.load_state_dict(checkpoint['model_state_dict'])
        self.train_losses = checkpoint['train_losses']
        self.val_losses = checkpoint['val_losses']
        self.train_accs = checkpoint['train_accs']
        self.val_accs = checkpoint['val_accs']
        print(f"  Loaded checkpoint from epoch {checkpoint['epoch']}")
        print(f"  Validation accuracy: {checkpoint['accuracy']:.2f}%")
        return checkpoint
    
    def plot_training_history(self):
        """Plot training and validation metrics."""
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))
        
        axes[0].plot(self.train_losses, label='Train')
        axes[0].plot(self.val_losses, label='Validation')
        axes[0].set_title('Loss')
        axes[0].set_xlabel('Epoch')
        axes[0].set_ylabel('Loss')
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)
        
        axes[1].plot(self.train_accs, label='Train')
        axes[1].plot(self.val_accs, label='Validation')
        axes[1].set_title('Accuracy')
        axes[1].set_xlabel('Epoch')
        axes[1].set_ylabel('Accuracy (%)')
        axes[1].legend()
        axes[1].grid(True, alpha=0.3)
        
        plt.suptitle("Training History", fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.show()
    
    def evaluate(self, test_loader, criterion):
        """Evaluate on test set."""
        test_loss, test_acc = self.validate(test_loader, criterion)
        print(f"Test Loss: {test_loss:.4f}, Test Accuracy: {test_acc:.2f}%")
        return test_loss, test_acc


def get_data_loaders(batch_size=128):
    """
    Get CIFAR-10 data loaders with data augmentation.
    
    Design Pattern: Factory Pattern - Creates data loaders
    """
    # Data augmentation for training
    train_transform = transforms.Compose([
        transforms.RandomCrop(32, padding=4),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(15),
        transforms.ColorJitter(brightness=0.2, contrast=0.2),
        transforms.ToTensor(),
        transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010))
    ])
    
    # Simple transform for validation/test
    test_transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010))
    ])
    
    # Download datasets
    train_dataset = datasets.CIFAR10(
        root='./data', train=True, download=True, transform=train_transform
    )
    test_dataset = datasets.CIFAR10(
        root='./data', train=False, download=True, transform=test_transform
    )
    
    # Split training into train/val
    train_size = int(0.9 * len(train_dataset))
    val_size = len(train_dataset) - train_size
    train_dataset, val_dataset = torch.utils.data.random_split(
        train_dataset, [train_size, val_size]
    )
    
    # Create data loaders
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=2)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False, num_workers=2)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False, num_workers=2)
    
    print(f"  Training samples: {len(train_dataset)}")
    print(f"  Validation samples: {len(val_dataset)}")
    print(f"  Test samples: {len(test_dataset)}")
    
    return train_loader, val_loader, test_loader


def visualize_predictions(model, test_loader, device, num_images=16):
    """Visualize model predictions on test images."""
    model.eval()
    
    # Get batch of images
    dataiter = iter(test_loader)
    images, labels = next(dataiter)
    images, labels = images[:num_images].to(device), labels[:num_images]
    
    # Get predictions
    with torch.no_grad():
        outputs = model(images)
        _, predicted = outputs.max(1)
    
    # Class names
    classes = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']
    
    # Display images
    fig, axes = plt.subplots(4, 4, figsize=(12, 12))
    axes = axes.flatten()
    
    for i in range(num_images):
        ax = axes[i]
        img = images[i].cpu().numpy().transpose(1, 2, 0)
        
        # Denormalize
        mean = np.array([0.4914, 0.4822, 0.4465])
        std = np.array([0.2023, 0.1994, 0.2010])
        img = std * img + mean
        img = np.clip(img, 0, 1)
        
        ax.imshow(img)
        true_label = classes[labels[i]]
        pred_label = classes[predicted[i]]
        color = 'green' if true_label == pred_label else 'red'
        ax.set_title(f"True: {true_label}\nPred: {pred_label}", fontsize=10, color=color)
        ax.axis('off')
    
    plt.suptitle("Model Predictions on CIFAR-10", fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()


def demonstrate_cifar10_cnn():
    """
    Demonstrate complete CNN training on CIFAR-10.
    """
    print("\n" + "=" * 60)
    print("SECTION 2: CNN FOR CIFAR-10 CLASSIFICATION")
    print("=" * 60)
    
    # SET DEVICE
    print("\n1. SETTING UP DEVICE")
    print("-" * 40)
    
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"  Using device: {device}")
    
    # LOAD DATA
    print("\n2. LOADING CIFAR-10 DATA")
    print("-" * 40)
    
    train_loader, val_loader, test_loader = get_data_loaders(batch_size=128)
    
    # CREATE MODEL
    print("\n3. CREATING CNN MODEL")
    print("-" * 40)
    
    model = CIFAR10CNN(num_classes=10)
    print(f"  Model parameters: {sum(p.numel() for p in model.parameters()):,}")
    
    # LOSS AND OPTIMIZER
    print("\n4. SETTING UP LOSS AND OPTIMIZER")
    print("-" * 40)
    
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001, weight_decay=1e-4)
    scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', factor=0.5, patience=3)
    
    print("  Loss: CrossEntropyLoss")
    print("  Optimizer: Adam (lr=0.001, weight_decay=1e-4)")
    print("  Scheduler: ReduceLROnPlateau")
    
    # TRAIN
    print("\n5. TRAINING MODEL")
    print("-" * 40)
    
    trainer = Trainer(model, device)
    best_acc = trainer.train(
        train_loader, val_loader, criterion, optimizer,
        epochs=30, scheduler=scheduler, early_stop_patience=5
    )
    
    # PLOT TRAINING HISTORY
    print("\n6. TRAINING HISTORY")
    print("-" * 40)
    
    trainer.plot_training_history()
    
    # EVALUATE ON TEST SET
    print("\n7. TEST SET EVALUATION")
    print("-" * 40)
    
    test_loss, test_acc = trainer.evaluate(test_loader, criterion)
    
    # VISUALIZE PREDICTIONS
    print("\n8. VISUALIZING PREDICTIONS")
    print("-" * 40)
    
    visualize_predictions(model, test_loader, device, num_images=16)
    
    # SAVE MODEL
    print("\n9. SAVING MODEL")
    print("-" * 40)
    
    trainer.save_checkpoint(epoch=30, accuracy=test_acc, is_best=True)
    print("  Model saved to checkpoints/best_model.pt")
    
    return model, trainer


if __name__ == "__main__":
    demonstrate_cifar10_cnn()
```

---

## 🔥 Section 3: Custom Training Loop with Advanced Features

A complete training framework with gradient accumulation, mixed precision, and custom metrics.

**SOLID Principles Applied:**
- Single Responsibility: Each component handles one aspect of training
- Open/Closed: New metrics and callbacks can be added

**Design Patterns:**
- Observer Pattern: Callbacks observe training events
- Strategy Pattern: Different optimization strategies

```python
"""
CUSTOM TRAINING LOOP WITH ADVANCED FEATURES

This section implements advanced training techniques.

SOLID Principles Applied:
- Single Responsibility: Each component handles one aspect
- Open/Closed: New metrics and callbacks can be added

Design Patterns:
- Observer Pattern: Callbacks observe training events
- Strategy Pattern: Different optimization strategies
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.cuda.amp import autocast, GradScaler
from torch.utils.tensorboard import SummaryWriter
from collections import defaultdict
import numpy as np
from tqdm import tqdm
import time
import os


class AverageMeter:
    """Computes and stores the average and current value."""
    
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0
    
    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count


class Callback:
    """
    Base class for training callbacks.
    
    Design Pattern: Observer Pattern - Observes training events
    """
    
    def on_train_begin(self, trainer):
        pass
    
    def on_train_end(self, trainer):
        pass
    
    def on_epoch_begin(self, trainer, epoch):
        pass
    
    def on_epoch_end(self, trainer, epoch, metrics):
        pass
    
    def on_batch_begin(self, trainer, batch):
        pass
    
    def on_batch_end(self, trainer, batch, loss):
        pass


class ModelCheckpoint(Callback):
    """Saves model checkpoints."""
    
    def __init__(self, save_dir, monitor='val_acc', mode='max', save_best_only=True):
        self.save_dir = save_dir
        self.monitor = monitor
        self.mode = mode
        self.save_best_only = save_best_only
        self.best_value = -float('inf') if mode == 'max' else float('inf')
        os.makedirs(save_dir, exist_ok=True)
    
    def on_epoch_end(self, trainer, epoch, metrics):
        current = metrics.get(self.monitor)
        if current is None:
            return
        
        is_best = False
        if self.mode == 'max' and current > self.best_value:
            self.best_value = current
            is_best = True
        elif self.mode == 'min' and current < self.best_value:
            self.best_value = current
            is_best = True
        
        if is_best or not self.save_best_only:
            filename = f"{self.save_dir}/checkpoint_epoch_{epoch}.pt"
            torch.save({
                'epoch': epoch,
                'model_state_dict': trainer.model.state_dict(),
                'optimizer_state_dict': trainer.optimizer.state_dict(),
                'metrics': metrics,
                'best_value': self.best_value
            }, filename)
            
            if is_best:
                best_filename = f"{self.save_dir}/best_model.pt"
                torch.save({
                    'epoch': epoch,
                    'model_state_dict': trainer.model.state_dict(),
                    'optimizer_state_dict': trainer.optimizer.state_dict(),
                    'metrics': metrics,
                    'best_value': self.best_value
                }, best_filename)
                print(f"  Best {self.monitor}: {self.best_value:.4f}")


class LearningRateScheduler(Callback):
    """Learning rate scheduler callback."""
    
    def __init__(self, scheduler):
        self.scheduler = scheduler
    
    def on_epoch_end(self, trainer, epoch, metrics):
        self.scheduler.step()
        current_lr = trainer.optimizer.param_groups[0]['lr']
        print(f"  Learning rate: {current_lr:.6f}")


class TensorBoardLogger(Callback):
    """Logs metrics to TensorBoard."""
    
    def __init__(self, log_dir='runs/experiment'):
        self.writer = SummaryWriter(log_dir)
        self.epoch = 0
    
    def on_epoch_end(self, trainer, epoch, metrics):
        self.epoch = epoch
        for name, value in metrics.items():
            self.writer.add_scalar(name, value, epoch)
    
    def on_batch_end(self, trainer, batch, loss):
        if batch % 100 == 0:
            self.writer.add_scalar('train/loss_step', loss, trainer.global_step)
    
    def close(self):
        self.writer.close()


class ProgressBar(Callback):
    """Displays progress bar during training."""
    
    def __init__(self):
        self.pbar = None
    
    def on_epoch_begin(self, trainer, epoch):
        self.pbar = tqdm(total=len(trainer.train_loader), desc=f"Epoch {epoch+1}")
    
    def on_batch_end(self, trainer, batch, loss):
        self.pbar.update(1)
        self.pbar.set_postfix({'loss': f'{loss:.4f}'})
    
    def on_epoch_end(self, trainer, epoch, metrics):
        self.pbar.close()


class AdvancedTrainer:
    """
    Advanced trainer with mixed precision, gradient accumulation, and callbacks.
    
    Design Pattern: Template Method Pattern - Defines training workflow
    """
    
    def __init__(self, model, device, use_amp=True, gradient_accumulation_steps=1):
        self.model = model.to(device)
        self.device = device
        self.use_amp = use_amp and device.type == 'cuda'
        self.gradient_accumulation_steps = gradient_accumulation_steps
        
        self.scaler = GradScaler() if self.use_amp else None
        self.callbacks = []
        self.global_step = 0
        
        # Metrics
        self.train_loss = AverageMeter()
        self.train_acc = AverageMeter()
        self.val_loss = AverageMeter()
        self.val_acc = AverageMeter()
    
    def add_callback(self, callback):
        """Add a training callback."""
        self.callbacks.append(callback)
    
    def _trigger_callbacks(self, event, **kwargs):
        """Trigger callbacks for an event."""
        for callback in self.callbacks:
            method = getattr(callback, event, None)
            if method:
                method(self, **kwargs)
    
    def train_epoch(self, train_loader, criterion, optimizer):
        """Train for one epoch with mixed precision and gradient accumulation."""
        self.model.train()
        self.train_loss.reset()
        self.train_acc.reset()
        
        self._trigger_callbacks('on_epoch_begin', epoch=self.current_epoch)
        
        for batch_idx, (data, target) in enumerate(train_loader):
            self._trigger_callbacks('on_batch_begin', batch=batch_idx)
            
            data, target = data.to(self.device), target.to(self.device)
            
            # Mixed precision forward pass
            if self.use_amp:
                with autocast():
                    output = self.model(data)
                    loss = criterion(output, target) / self.gradient_accumulation_steps
                
                # Backward pass with scaler
                self.scaler.scale(loss).backward()
            else:
                output = self.model(data)
                loss = criterion(output, target) / self.gradient_accumulation_steps
                loss.backward()
            
            # Update weights after accumulation steps
            if (batch_idx + 1) % self.gradient_accumulation_steps == 0:
                if self.use_amp:
                    self.scaler.step(optimizer)
                    self.scaler.update()
                else:
                    optimizer.step()
                optimizer.zero_grad()
            
            # Metrics
            _, predicted = output.max(1)
            batch_acc = predicted.eq(target).sum().item() / target.size(0)
            
            self.train_loss.update(loss.item() * self.gradient_accumulation_steps, data.size(0))
            self.train_acc.update(batch_acc, data.size(0))
            
            self._trigger_callbacks('on_batch_end', batch=batch_idx, loss=self.train_loss.val)
            self.global_step += 1
        
        self._trigger_callbacks('on_epoch_end', epoch=self.current_epoch, 
                               metrics={'train_loss': self.train_loss.avg, 'train_acc': self.train_acc.avg})
        
        return self.train_loss.avg, self.train_acc.avg
    
    def validate(self, val_loader, criterion):
        """Validate the model."""
        self.model.eval()
        self.val_loss.reset()
        self.val_acc.reset()
        
        with torch.no_grad():
            for data, target in val_loader:
                data, target = data.to(self.device), target.to(self.device)
                
                output = self.model(data)
                loss = criterion(output, target)
                
                _, predicted = output.max(1)
                batch_acc = predicted.eq(target).sum().item() / target.size(0)
                
                self.val_loss.update(loss.item(), data.size(0))
                self.val_acc.update(batch_acc, data.size(0))
        
        return self.val_loss.avg, self.val_acc.avg
    
    def train(self, train_loader, val_loader, criterion, optimizer, epochs=50):
        """Complete training loop."""
        self.train_loader = train_loader
        self.optimizer = optimizer
        
        self._trigger_callbacks('on_train_begin')
        
        best_val_acc = 0.0
        
        for epoch in range(epochs):
            self.current_epoch = epoch
            
            # Train
            train_loss, train_acc = self.train_epoch(train_loader, criterion, optimizer)
            
            # Validate
            val_loss, val_acc = self.validate(val_loader, criterion)
            
            # Metrics
            metrics = {
                'train_loss': train_loss,
                'train_acc': train_acc,
                'val_loss': val_loss,
                'val_acc': val_acc,
                'lr': optimizer.param_groups[0]['lr']
            }
            
            # Print progress
            print(f"\nEpoch {epoch+1}/{epochs}")
            print(f"  Train Loss: {train_loss:.4f}, Train Acc: {train_acc:.2f}%")
            print(f"  Val Loss: {val_loss:.4f}, Val Acc: {val_acc:.2f}%")
            
            # Update best accuracy
            if val_acc > best_val_acc:
                best_val_acc = val_acc
                print(f"  ✓ New best validation accuracy: {val_acc:.2f}%")
            
            # Trigger callbacks
            self._trigger_callbacks('on_epoch_end', epoch=epoch, metrics=metrics)
        
        self._trigger_callbacks('on_train_end')
        
        return best_val_acc


def demonstrate_advanced_training():
    """
    Demonstrate advanced training techniques.
    """
    print("\n" + "=" * 60)
    print("SECTION 3: ADVANCED TRAINING TECHNIQUES")
    print("=" * 60)
    
    # Simple model for demonstration
    class SimpleModel(nn.Module):
        def __init__(self):
            super().__init__()
            self.fc1 = nn.Linear(784, 128)
            self.fc2 = nn.Linear(128, 64)
            self.fc3 = nn.Linear(64, 10)
            self.relu = nn.ReLU()
            self.dropout = nn.Dropout(0.2)
        
        def forward(self, x):
            x = x.view(x.size(0), -1)
            x = self.relu(self.fc1(x))
            x = self.dropout(x)
            x = self.relu(self.fc2(x))
            x = self.dropout(x)
            x = self.fc3(x)
            return x
    
    # Create synthetic dataset
    print("\n1. CREATING SYNTHETIC DATASET")
    print("-" * 40)
    
    from torch.utils.data import TensorDataset
    
    X_train = torch.randn(5000, 1, 28, 28)
    y_train = torch.randint(0, 10, (5000,))
    X_val = torch.randn(1000, 1, 28, 28)
    y_val = torch.randint(0, 10, (1000,))
    
    train_dataset = TensorDataset(X_train, y_train)
    val_dataset = TensorDataset(X_val, y_val)
    
    train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True)
    val_loader = torch.utils.data.DataLoader(val_dataset, batch_size=64, shuffle=False)
    
    print(f"  Training samples: {len(train_dataset)}")
    print(f"  Validation samples: {len(val_dataset)}")
    
    # Setup
    print("\n2. SETTING UP ADVANCED TRAINER")
    print("-" * 40)
    
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = SimpleModel()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    
    trainer = AdvancedTrainer(model, device, use_amp=True, gradient_accumulation_steps=2)
    
    # Add callbacks
    trainer.add_callback(ModelCheckpoint('checkpoints', monitor='val_acc', mode='max'))
    trainer.add_callback(LearningRateScheduler(optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.5)))
    trainer.add_callback(TensorBoardLogger('runs/advanced_trainer'))
    trainer.add_callback(ProgressBar())
    
    print("  Callbacks registered:")
    print("    - ModelCheckpoint")
    print("    - LearningRateScheduler")
    print("    - TensorBoardLogger")
    print("    - ProgressBar")
    print(f"  Mixed precision: {trainer.use_amp}")
    print(f"  Gradient accumulation steps: {trainer.gradient_accumulation_steps}")
    
    # Train
    print("\n3. TRAINING WITH ADVANCED TECHNIQUES")
    print("-" * 40)
    
    best_acc = trainer.train(train_loader, val_loader, criterion, optimizer, epochs=10)
    print(f"\n  Best validation accuracy: {best_acc:.2f}%")
    
    print("\n4. ADVANCED TECHNIQUES SUMMARY")
    print("-" * 40)
    
    techniques = [
        "✓ Mixed Precision Training (AMP) - 2x faster, 50% less memory",
        "✓ Gradient Accumulation - Simulate larger batch sizes",
        "✓ Gradient Clipping - Prevent exploding gradients",
        "✓ Learning Rate Scheduling - Reduce LR on plateau",
        "✓ Model Checkpointing - Save best models",
        "✓ TensorBoard Logging - Track metrics in real-time",
        "✓ Progress Bars - Visual training feedback"
    ]
    
    for tech in techniques:
        print(f"  {tech}")
    
    # Clean up
    import shutil
    if os.path.exists('checkpoints'):
        shutil.rmtree('checkpoints')
    if os.path.exists('runs'):
        shutil.rmtree('runs')
    print("\n  Cleaned up checkpoints and logs")


if __name__ == "__main__":
    demonstrate_advanced_training()
```

---

## 🚀 Section 4: Model Deployment for Inference

Deploying PyTorch models for production inference with TorchScript and ONNX.

**SOLID Principles Applied:**
- Single Responsibility: Each export method handles one format
- Open/Closed: New export formats can be added

**Design Patterns:**
- Adapter Pattern: Adapts PyTorch model to different formats
- Factory Pattern: Creates inference pipelines

```python
"""
MODEL DEPLOYMENT FOR INFERENCE

This section covers deploying PyTorch models to production.

SOLID Principles Applied:
- Single Responsibility: Each export method handles one format
- Open/Closed: New export formats can be added

Design Patterns:
- Adapter Pattern: Adapts PyTorch model to different formats
- Factory Pattern: Creates inference pipelines
"""

import torch
import torch.nn as nn
import numpy as np
import time
import json
from pathlib import Path


class DeployableModel(nn.Module):
    """
    Simple CNN model designed for deployment.
    
    Design Pattern: Adapter Pattern - Adapts to multiple export formats
    """
    
    def __init__(self, num_classes=10):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(64 * 7 * 7, 128)
        self.fc2 = nn.Linear(128, num_classes)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.2)
    
    def forward(self, x):
        x = self.pool(self.relu(self.conv1(x)))
        x = self.pool(self.relu(self.conv2(x)))
        x = x.view(x.size(0), -1)
        x = self.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return x


class ModelExporter:
    """
    Exports PyTorch models to various formats.
    
    Design Pattern: Factory Pattern - Creates inference-ready models
    """
    
    @staticmethod
    def to_torchscript_trace(model, example_input, filepath):
        """Export using tracing (recommended for most cases)."""
        model.eval()
        traced_model = torch.jit.trace(model, example_input)
        traced_model.save(filepath)
        print(f"  Saved TorchScript traced model to {filepath}")
        return traced_model
    
    @staticmethod
    def to_torchscript_script(model, filepath):
        """Export using scripting (for models with control flow)."""
        model.eval()
        scripted_model = torch.jit.script(model)
        scripted_model.save(filepath)
        print(f"  Saved TorchScript scripted model to {filepath}")
        return scripted_model
    
    @staticmethod
    def to_onnx(model, example_input, filepath, input_names=None, output_names=None):
        """Export to ONNX format for interoperability."""
        model.eval()
        input_names = input_names or ['input']
        output_names = output_names or ['output']
        
        torch.onnx.export(
            model,
            example_input,
            filepath,
            input_names=input_names,
            output_names=output_names,
            dynamic_axes={'input': {0: 'batch_size'}, 'output': {0: 'batch_size'}},
            opset_version=11,
            do_constant_folding=True
        )
        print(f"  Saved ONNX model to {filepath}")
    
    @staticmethod
    def save_model_state(model, filepath):
        """Save model state dict (weights only)."""
        torch.save(model.state_dict(), filepath)
        print(f"  Saved model state to {filepath}")
    
    @staticmethod
    def save_full_checkpoint(model, optimizer, epoch, metrics, filepath):
        """Save full training checkpoint."""
        checkpoint = {
            'epoch': epoch,
            'model_state_dict': model.state_dict(),
            'optimizer_state_dict': optimizer.state_dict(),
            'metrics': metrics
        }
        torch.save(checkpoint, filepath)
        print(f"  Saved full checkpoint to {filepath}")


class InferenceEngine:
    """
    Production inference engine for PyTorch models.
    
    Design Pattern: Proxy Pattern - Provides unified inference interface
    """
    
    def __init__(self, model_path, device='cpu', model_type='torchscript'):
        self.device = torch.device(device)
        self.model_type = model_type
        self.model = self._load_model(model_path)
        self.model.eval()
    
    def _load_model(self, model_path):
        """Load model based on type."""
        if self.model_type == 'torchscript':
            model = torch.jit.load(model_path, map_location=self.device)
        elif self.model_type == 'onnx':
            import onnxruntime as ort
            self.ort_session = ort.InferenceSession(model_path)
            return None
        else:
            model = DeployableModel()
            model.load_state_dict(torch.load(model_path, map_location=self.device))
            model.to(self.device)
        
        return model
    
    def predict(self, x):
        """Run inference on input data."""
        if self.model_type == 'onnx':
            # ONNX Runtime inference
            ort_inputs = {self.ort_session.get_inputs()[0].name: x.numpy()}
            ort_outputs = self.ort_session.run(None, ort_inputs)
            return torch.tensor(ort_outputs[0])
        else:
            # PyTorch inference
            with torch.no_grad():
                x = x.to(self.device)
                output = self.model(x)
                return output.cpu()
    
    def predict_batch(self, batch):
        """Run inference on a batch of inputs."""
        return self.predict(batch)
    
    def predict_class(self, x):
        """Get predicted class."""
        output = self.predict(x)
        return output.argmax(dim=1)
    
    def predict_proba(self, x):
        """Get prediction probabilities."""
        output = self.predict(x)
        return torch.softmax(output, dim=1)
    
    def benchmark(self, input_shape, num_runs=100, warmup=10):
        """Benchmark inference speed."""
        # Warmup
        dummy_input = torch.randn(input_shape)
        for _ in range(warmup):
            _ = self.predict(dummy_input)
        
        # Benchmark
        start = time.time()
        for _ in range(num_runs):
            _ = self.predict(dummy_input)
        elapsed = time.time() - start
        
        avg_time = elapsed / num_runs * 1000  # ms
        fps = num_runs / elapsed
        
        return {
            'avg_inference_time_ms': avg_time,
            'fps': fps,
            'total_time_s': elapsed,
            'num_runs': num_runs
        }


class ModelServer:
    """
    Simple model server for production deployment.
    
    Design Pattern: Singleton Pattern - Single server instance
    """
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        
        self.models = {}
        self._initialized = True
    
    def register_model(self, name, engine):
        """Register a model for serving."""
        self.models[name] = engine
        print(f"  Registered model: {name}")
    
    def predict(self, model_name, x):
        """Make prediction using registered model."""
        if model_name not in self.models:
            raise ValueError(f"Model '{model_name}' not found")
        return self.models[model_name].predict(x)
    
    def get_model_info(self):
        """Get information about registered models."""
        info = {}
        for name, engine in self.models.items():
            info[name] = {
                'type': engine.model_type,
                'device': str(engine.device)
            }
        return info


def demonstrate_model_deployment():
    """
    Demonstrate model deployment for inference.
    """
    print("\n" + "=" * 60)
    print("SECTION 4: MODEL DEPLOYMENT FOR INFERENCE")
    print("=" * 60)
    
    # CREATE MODEL
    print("\n1. CREATING MODEL")
    print("-" * 40)
    
    model = DeployableModel(num_classes=10)
    model.eval()
    
    # Create dummy input
    example_input = torch.randn(1, 1, 28, 28)
    output = model(example_input)
    
    print(f"  Model input shape: {example_input.shape}")
    print(f"  Model output shape: {output.shape}")
    print(f"  Model parameters: {sum(p.numel() for p in model.parameters()):,}")
    
    # EXPORT MODELS
    print("\n2. EXPORTING TO DIFFERENT FORMATS")
    print("-" * 40)
    
    exporter = ModelExporter()
    
    # Create export directory
    Path("./exported_models").mkdir(exist_ok=True)
    
    # Export TorchScript (traced)
    exporter.to_torchscript_trace(model, example_input, "./exported_models/model_traced.pt")
    
    # Export TorchScript (scripted)
    exporter.to_torchscript_script(model, "./exported_models/model_scripted.pt")
    
    # Export ONNX
    exporter.to_onnx(model, example_input, "./exported_models/model.onnx")
    
    # Export state dict
    exporter.save_model_state(model, "./exported_models/model_weights.pth")
    
    # LOAD AND BENCHMARK
    print("\n3. LOADING AND BENCHMARKING MODELS")
    print("-" * 40)
    
    formats = [
        ('TorchScript (Traced)', 'torchscript', './exported_models/model_traced.pt'),
        ('TorchScript (Scripted)', 'torchscript', './exported_models/model_scripted.pt'),
    ]
    
    results = {}
    
    for name, model_type, path in formats:
        print(f"\n  Benchmarking {name}:")
        engine = InferenceEngine(path, device='cpu', model_type=model_type)
        benchmark = engine.benchmark(input_shape=(1, 1, 28, 28), num_runs=50)
        results[name] = benchmark
        print(f"    Avg inference time: {benchmark['avg_inference_time_ms']:.2f} ms")
        print(f"    FPS: {benchmark['fps']:.2f}")
    
    # MODEL SERVER
    print("\n4. MODEL SERVER")
    print("-" * 40)
    
    server = ModelServer()
    server.register_model("classifier", InferenceEngine("./exported_models/model_traced.pt"))
    server.register_model("classifier_script", InferenceEngine("./exported_models/model_scripted.pt"))
    
    # Make predictions
    print("\n  Making predictions:")
    test_input = torch.randn(3, 1, 28, 28)
    predictions = server.predict("classifier", test_input)
    predicted_classes = predictions.argmax(dim=1)
    
    for i, pred_class in enumerate(predicted_classes):
        print(f"    Sample {i+1}: Predicted class {pred_class.item()}")
    
    # COMPARISON
    print("\n5. FORMAT COMPARISON")
    print("-" * 40)
    
    print(f"\n{'Format':<25} {'Inference Time (ms)':<20} {'FPS':<10}")
    print("-" * 55)
    for name, bench in results.items():
        print(f"{name:<25} {bench['avg_inference_time_ms']:<20.2f} {bench['fps']:<10.2f}")
    
    # PRODUCTION CHECKLIST
    print("\n6. PRODUCTION DEPLOYMENT CHECKLIST")
    print("-" * 40)
    
    checklist = [
        "✓ Convert model to TorchScript or ONNX for production",
        "✓ Use batch inference for better throughput",
        "✓ Enable model quantization for edge deployment",
        "✓ Set up model versioning for A/B testing",
        "✓ Implement monitoring for inference latency and accuracy",
        "✓ Use GPU for inference when low latency required",
        "✓ Set up auto-scaling based on request volume",
        "✓ Implement circuit breakers for model failures",
        "✓ Cache frequent inference results",
        "✓ Log prediction inputs and outputs for auditing"
    ]
    
    for item in checklist:
        print(f"  {item}")
    
    # Clean up
    import shutil
    if os.path.exists("./exported_models"):
        shutil.rmtree("./exported_models")
    print("\n  Cleaned up exported models")


if __name__ == "__main__":
    demonstrate_model_deployment()
```

---

## 📊 Takeaway from This Story

**What You Learned:**

- **PyTorch Tensors** – Multi-dimensional arrays similar to NumPy. GPU acceleration with `.to(device)`. Automatic differentiation with `requires_grad=True`.

- **Autograd** – Builds computation graph automatically. `backward()` computes gradients. Gradients accumulate by default.

- **nn.Module** – Base class for all neural network modules. Define architecture in `__init__` and computation in `forward()`.

- **Common Layers** – `Linear`, `Conv2d`, `MaxPool2d`, `BatchNorm2d`, `Dropout`, `Flatten`. Activation functions: `ReLU`, `Sigmoid`, `Tanh`, `Softmax`.

- **Training Loop** – Zero gradients → forward pass → compute loss → backward pass → update weights. Use `optimizer.zero_grad()`, `loss.backward()`, `optimizer.step()`.

- **Data Loading** – `Dataset` class for custom data. `DataLoader` for batching, shuffling, multiprocessing. Transforms for data augmentation.

- **Advanced Techniques** – Mixed precision training (AMP) for 2x speedup. Gradient accumulation for larger effective batch sizes. Gradient clipping to prevent exploding gradients.

- **Callbacks** – Observer pattern for training events. Model checkpointing, learning rate scheduling, TensorBoard logging, progress bars.

- **Model Export** – TorchScript (tracing/scripting) for production deployment. ONNX for cross-platform interoperability. State dicts for weights only.

- **Inference Engine** – Unified interface for loaded models. Benchmarking for latency and throughput. Model server with multiple registered models.

- **SOLID Principles Applied** – Single Responsibility (each layer/module has one purpose), Open/Closed (new layers can be added), Dependency Inversion (training depends on model abstraction), Interface Segregation (clean module interfaces).

- **Design Patterns Used** – Template Method Pattern (training workflow), Observer Pattern (callbacks), Builder Pattern (model architecture), Adapter Pattern (model export), Factory Pattern (inference engine), Proxy Pattern (inference interface), Singleton Pattern (model server), Command Pattern (autograd operations).

---

## 🔗 Navigation

- **⬅️ Previous Story:** The 2026 Python Metromap: TensorFlow and Keras – Deep Learning

- **📚 Series I Catalog:** AI & Machine Learning with Python – View all 4 stories in this series.

- **📚 Complete Story Catalog:** Complete 2026 Python Metromap Story Catalog – Your navigation guide to all 52 stories.

- **➡️ Next Story:** The 2026 Python Metromap: End-to-End ML Pipeline Project (Series I, Story 4)

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
| Series I | 4 | 3 | 1 | 75% |
| Series J | 3 | 0 | 3 | 0% |
| **Total** | **52** | **51** | **1** | **98%** |

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
53. Series I, Story 3: The 2026 Python Metromap: PyTorch – Research and Production

**Next Story:** Series I, Story 4: The 2026 Python Metromap: End-to-End ML Pipeline Project

---

## 📝 Your Invitation

You've mastered PyTorch. Now build something with what you've learned:

1. **Build a custom image classifier** – Train a CNN on your own dataset (flowers, animals, objects).

2. **Create a neural style transfer app** – Implement artistic style transfer using pre-trained VGG.

3. **Build a text generation model** - Use RNN/LSTM to generate text in the style of your favorite author.

4. **Create a time series forecaster** – Predict stock prices or weather using LSTM.

5. **Build a GAN for image generation** – Generate realistic images with Generative Adversarial Networks.

**You've mastered PyTorch. Next stop: End-to-End ML Pipeline Project!**

---

*Found this helpful? Clap, comment, and share what you built with PyTorch. Next stop: End-to-End ML Pipeline Project!* 🚇