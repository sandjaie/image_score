"""
    Cli wrapper for findscore
"""
import click
from score.findscore import main as score
from score.configs import config as cfg

def helper():
    """Prints help message
    """
    print("""
        e.g imagescore --infile 'input.csv' --outfile 'output.csv'\n
        The options are:
        --infile | -i [str]    -- [Input file path]
        --outfile | -o [str]   -- [Output file path]
        --height | -h [int]    -- [Optional: height to be resized, default = 4096]
        --width | -w [int]     -- [Optional: width to be resized, default = 4096]
    """)

@click.command()
@click.option('--infile', '-i', help="Enter the input file path")
@click.option('--outfile', '-o', help="Enter the output file path")
@click.option('--height', '-h', type=int, help="[optional] height of the image to be resized, default = 4096")
@click.option('--width', '-w', type=int, help="[optional] Width of the image to be resized, default = 4096")
def main(infile, outfile, height, width):
    """
    This tool compares a set of images and returns the similarity score\n
    e.g imagescore --infile 'input.csv' --outfile 'output.csv'\n
    e.g imagescore -i 'input.csv' -o 'output.csv -h 1024 -w 1024'
    """
    try:
        if height is None and width is None:
            score(infile, outfile, height=cfg.HEIGHT, width=cfg.WIDTH)
        else:
            score(infile, outfile, height, width)
    except Exception:
        helper()
        print("Error: Missing options")
