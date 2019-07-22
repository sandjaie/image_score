## Bjorn score
### Calculate image similarity score
Expected Input: csv file with images and its absolute path <br>
Expected Output: csv file with images and its absolute path, image score and elapsed time in secs. <br>
How to run? <br>
`imagescore --infile 'input.csv' --outfile 'output.csv'`

        The options are:
        --infile  | -i [str]    -- [Input file path]
        --outfile | -o [str]    -- [Output file path]
        --height  | -h [int]    -- [Optional: height to be resized, default = 4096]
        --width   | -w [int]    -- [Optional: width to be resized, default = 4096]
Developer mode: <br>
`pip install -e .`