import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
from torchvision.datasets import CIFAR10
from torch.utils.data import DataLoader
import torchapprox.layers as tal
from torchapprox.utils import wrap_quantizable, get_approx_modules
import numpy as np
from temp import multiply2

def evaluate_with_approx_multiplier():
    # Check for GPU availability
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    # Load a pretrained model
    print("Loading MobileNetV2 model...")
    model = models.mobilenet_v2(pretrained=True).to(device)
    model.eval()  # Set the model to evaluation mode
    print("Model loaded successfully!")

    # Wrap Linear and Conv2d layers for quantization
    print("Wrapping layers for quantization...")
    try:
        wrap_quantizable(model)
        print("Wrapping completed.")
    except Exception as e:
        print(f"Error during wrapping layers: {e}")
        return None

    # Replace LUT-based multiplication with the custom multiply2 function
    print("Setting up approximate multiplication using multiply2...")
    def set_custom_approx_forward(model):
        """Set custom approximate forward pass using multiply2."""
        for name, module in get_approx_modules(model):
            if hasattr(module, 'approx_fwd'):
                module.approx_fwd = lambda x, y: multiply2(x, y)  # Replace with custom multiply2 function
                module.inference_mode = tal.InferenceMode.APPROXIMATE
                print(f"Set custom approx_fwd for module: {name}")
            else:
                print(f"Module {name} does not support approx_fwd.")

    # Apply the custom approximate multiplication
    try:
        set_custom_approx_forward(model)
        print("Custom approximate multiplication set successfully.")
    except Exception as e:
        print(f"Error setting custom approximate multiplication: {e}")
        return None

    # Set up the dataset and data loaders
    print("Setting up CIFAR-10 dataset...")
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))  # ImageNet mean and std
    ])

    test_dataset = CIFAR10(root='./data', train=False, download=True, transform=transform)
    test_loader = DataLoader(test_dataset, batch_size=256, shuffle=False, pin_memory=True, num_workers=8)
    print("Dataset and data loaders ready.")

    # Validate the model
    print("Validating the model...")
    correct = 0
    total = 0
    model.eval()
    with torch.no_grad():
        for inputs, labels in test_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)  # Forward pass uses custom approx_fwd internally
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    accuracy = 100 * correct / total
    print(f"Validation complete. Accuracy on test set: {accuracy:.2f}%")

    return accuracy

# Call the function and get the accuracy
accuracy = evaluate_with_approx_multiplier()
print(f"Model Accuracy with Approximate Multiplication: {accuracy:.2f}%")
