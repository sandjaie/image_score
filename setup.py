from setuptools import setup, find_packages

requirements = [
    "opencv-python",
    "scikit-image",
    "click"
]

setup(
    name='imagescore',
    description='Calculates the similarity score between images',
    classifiers = [
        'Operating System :: OS Independent',
        'Environment :: CLI',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7'
    ],
    author='sandjaie',
    url='https://github.com/sandjaie/image_score',
    version='1.0.0',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'imagescore=score.cli:main'
        ]
    }
)