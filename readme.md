# ComfyUI BEN (Background Erase Network)

****


Remove backgrounds from images with [BEN](https://huggingface.co/PramaLLC/BEN) in [ComfyUI](https://github.com/comfyanonymous/ComfyUI)

## Installation

```
git clone https://github.com/DoctorDiffusion/ComfyUI-BEN.git
```
```
cd ComfyUI-BEN
```
```
pip install -r requirements.txt
```
Go to [BEN Huggingface page](https://huggingface.co/PramaLLC/BEN/tree/main) and download BEN_Base.pth
```
```
cd ComfyUI-BEN
```
The folder should look like this:
└── ComfyUI/custom-nodes/ComfyUI-BEN/
    ├── __init__.py
    ├── background_erase_network.py
    ├── ben.png
    ├── BEN_Base.pth
    ├── model.py
    ├── readme.txt
    └── requirements.txt
```
## Nodes

### Background Erase Network

Outputs image of subject with alpha layer, combine with Image to Mask Node to get alpha mask as well.

## Credits

- [comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI)

- [PramaLLC/BEN](https://huggingface.co/PramaLLC/BEN)

⭐ If you like the project, please give it a star! ⭐

## License

While this is under an Apache 2.0 License, [PramaLLC](https://huggingface.co/PramaLLC/BEN) has restricted the use of their model for for commercial purposes. Reach out to them directly for more information.

