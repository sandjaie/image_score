## Bjorn score
[![Build Status](https://travis-ci.com/sandjaie/image_score.svg?branch=master)](https://travis-ci.com/sandjaie/image_score)

![PyPI](https://img.shields.io/pypi/v/imagescore.svg)

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/imagescore.svg)

### Calculate image similarity score

#### Tools used:
```
Language: Python
Dev Modules Used: 
- opencv-python
- scikit-image
- click
Test Modules Used:
- tox
- pytest
- pylint
- pytest-cov
Build and Deployment: Travis-ci
App Repository: PyPi 
```
#### Installation:<br>
`pip3 install imagescore`

#### How to run:<br>
`imagescore --infile 'input.csv' --outfile 'output.csv'`

#### The options are:<br>

        --infile  | -i [str]    -- [Input file path]
        --outfile | -o [str]    -- [Output file path]
        --height  | -h [int]    -- [Optional: height to be resized, default = 4096]
        --width   | -w [int]    -- [Optional: width to be resized, default = 4096]

Expected Input: csv file with images and its absolute path <br>
Expected Output: csv file with images and its absolute path, image score and elapsed time in secs. <br>


#### Developer mode: <br>
The application is written in python3. Hence create a virtualenv with python3 and install the dependencies from `requirements.txt`. 
```
virtualenv --python=python3 venv
pip install -e .
```

The unit test cases are located in tests directory. Install the dependencies `requrements-dev.txt`. 
```
pip install -r requirements-dev.txt
tox
```

#### Deployment: <br>
The python package is build with the travis.yml script when there are changes on the master branch. 
To push a new version:
Make the changes in the application, push it to any feature branch and merge with master.<br>
To deploy a new version tag it. e.g 
```
git tag -a v1.1.0
git push origin v1.1.0
```
When a tag is pushed, travis starts building and uploads the application to pypi<br>
Pypi Release: https://pypi.org/project/imagescore/<br>
Github Release: https://github.com/sandjaie/image_score/releases<br>
Travis Builds: https://travis-ci.com/sandjaie/image_score/<br>

Manual Deployment:<br>
We are using twine to upload the artifact to Pypi registry.
Pypi registry needs an account to be created. Enter the credentials in the cli when prompted.
```
pip3 install twine
python3 setup.py sdist bdist_wheel
twine upload dist/*
```
