# rlsa_python
This is a python implementation of the Run Length Smoothing Algorithm (RLSA). It was designed with text document layout analysis in mind in order to merge charatcters on the same line and make it easier to identify senteces and paragraphs.

## External requirements
rlsa_python only requires you to have numpy installed.

## Usage
### How to install it
```sh
$ pip install rlsa_python
```
### How to use it
```python
# Import RLSA class
from rlsa_python.rlsa import RLSA

img = # read in image and convert it to binary format (where the text is in white and background in black)...
smeared_text_image = RLSA.apply_rlsa(img, 100, 100, 50)
```
