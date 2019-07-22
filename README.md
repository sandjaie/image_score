## Bjorn score
### Calculate image similarity score
Expected Input: csv file with images and its absolute path <br>
Expected Output: csv file with images and its absolute path, image score and elapsed time in secs. <br>

Install:<br>
`pip3 install imagescore`

How to run:<br>
`imagescore --infile 'input.csv' --outfile 'output.csv'`

The options are:<br>

        --infile  | -i [str]    -- [Input file path]
        --outfile | -o [str]    -- [Output file path]
        --height  | -h [int]    -- [Optional: height to be resized, default = 4096]
        --width   | -w [int]    -- [Optional: width to be resized, default = 4096]

Developer mode: <br>
The application is written in python3. Hence create a virtualenv with python3 and install the dependencies. 
```
virtualenv --python=python3 venv
pip install -e .
```

Tests:<br>
The unit test cases are located in tests directory. Install the dependencies `requrements-dev.txt`. 
```
pip install -r requirements-dev.txt
tox
```