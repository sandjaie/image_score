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
@click.option('--height', '-h', type=int, help="[optional] Heigth to resize the image")
@click.option('--width', '-w', type=int, help="[optional] Width to resize the image")
def main(infile, outfile, height, width):
    """cli function for findscore
    """
    try:
        if height is None and width is None:
            score(infile, outfile, height=cfg.HEIGHT, width=cfg.WIDTH)
        else:
            score(infile, outfile, height, width)
    except Exception:
        helper()
        print("Error: Missing options")
