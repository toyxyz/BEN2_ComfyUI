import sys
import os
import torch
from PIL import Image
from torchvision import transforms

# Add the directory of the current file to sys.path
script_directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_directory)

# Now import BEN_Base from model.py
from model import BEN_Base

class BackgroundEraseNetwork:
    def __init__(self):
        self.model = BEN_Base()  # Initialize BEN_Base model
        self.model.loadcheckpoints("./ComfyUI/custom_nodes/ComfyUI-BEN/BEN_Base.pth")  # Load the model weights

        # Define transformations for converting between PIL and Tensor
        self.to_pil = transforms.ToPILImage()
        self.to_tensor = transforms.ToTensor()

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_image": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "process_image"
    CATEGORY = "BEN"

    def process_image(self, input_image):
        # Handle the input tensor format from ComfyUI
        if isinstance(input_image, torch.Tensor):
            if input_image.dim() == 4:
                input_image = input_image[0]
            
            if input_image.dim() == 3:
                input_image = input_image.permute(2, 0, 1)
            
            input_image = self.to_pil(input_image)

        # Ensure the image is in RGBA mode
        if input_image.mode != 'RGBA':
            input_image = input_image.convert("RGBA")

        # Run inference to get the foreground image
        _, foreground = self.model.inference(input_image)

        # Convert the foreground to tensor
        foreground_tensor = self.to_tensor(foreground)
        
        # Convert to ComfyUI format [B, H, W, C]
        foreground_tensor = foreground_tensor.permute(1, 2, 0).unsqueeze(0)
        
        return (foreground_tensor,)

# Export mappings for ComfyUI
NODE_CLASS_MAPPINGS = {
    "BackgroundEraseNetwork": BackgroundEraseNetwork
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "BackgroundEraseNetwork": "Background Erase Network"
}