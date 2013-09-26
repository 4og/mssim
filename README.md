MSSIM
=====
A simple implementation of the Mean Structural Similarity (MSSIM) algorithm as 
described in the paper: Zhou Wang et al. "Image quality assessment: From error
visibility to structural similarity". In: *Image Processing, IEEE Transactions
on* 13.4 (2004), pp. 600–612.

To run the code, you need to have [SciPy library](http://scipy.org) and 
[Python Imaging Library](http://www.pythonware.com/products/pil) (PIL). If you 
use Python 3, which is not supported by the PIL, please install one of PIL's forks, 
for example [Pillow](https://github.com/python-imaging/Pillow).

Usage: `./mssim.py REFERENCE_IMAGE OTHER_IMAGES...`

