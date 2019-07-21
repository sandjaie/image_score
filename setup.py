from setuptools import setup

with open('requirements.txt', 'rt') as rf:
    requirements = rf.readlines()

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
    packages=["score"],
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'imagescore=score.find_score:main'
        ]
    }
)