from setuptools import find_packages, setup
import sys

cv_ver = ""
keras_ver = ">=2.0.0"
if sys.version_info.major < 3:
    cv_ver = "<=4.2.0.32" 
    keras_ver = "<=2.3.0"

setup(
    name="keras_segmentation",
    version="0.3.0",
    description="Image Segmentation toolkit for keras",
    author="Divam Gupta",
    author_email='divamgupta@gmail.com',
    platforms=["any"],
    license="GPLv3",
    url="https://github.com/lbj-byte/image-segmentation-keras",
    packages=find_packages(exclude=["test"]),
    entry_points={
        'console_scripts': [
            'keras_segmentation = keras_segmentation.__main__:main'
        ]
    },
    install_requires=[
        # "Keras"+keras_ver,  # Removed to avoid installing h5py indirectly
        "imageio==2.5.0",
        "imgaug>=0.4.0",
        "opencv-python" + cv_ver,
        "tqdm"
    ],
    extras_require={
        "tensorflow": ["tensorflow"],
        "cntk": ["cntk"],
        "theano": ["theano"],
        "tests-default": ["tensorflow", "pytest"]
    }
)

