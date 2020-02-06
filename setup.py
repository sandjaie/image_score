from setuptools import setup, find_packages

requirements = [
    "opencv-python",
    "scikit-image",
    "click"
]
version = '1.1.0'
download_url = f'https://github.com/sandjaie/image_score/archive/{version}.tar.gz'

with open('README.md', 'r', errors='ignore') as fd:
    long_desc = fd.read()

setup(
    name='imagescore',
    description='Calculates the similarity score between images',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    author='sandjaie',
    url='https://github.com/sandjaie/image_score',
    author_email='sandjaie@gmail.com',
    version=version,
    packages=find_packages(),
    install_requires=requirements,
    download_url=download_url,
    license='MIT',
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7'
    ],
    entry_points={
        'console_scripts': [
            'imagescore=score.cli:main'
        ]
    }
)