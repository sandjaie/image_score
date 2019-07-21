import click
from score.findscore import main as score
from score.configs import config as cfg

def helper():
    print("""
        e.g imagescore --infile 'input.csv' --outfile '/tmp/output.csv'\n
        The options are:
        infile [str]    -- [Input file path]
        outfile [str]   -- [Output file path]
        height [int]    -- [Optional: height to be resized, default = 4096]
        width [int]     -- [Optional: width to be resized, default = 4096]
    """)


@click.command()
@click.option('--infile', '-i', help="Enter the input file path")
@click.option('--outfile', '-o', help="Enter the output file path")
@click.option('--height', '-h', type=int, help="Heigth to resize the image")
@click.option('--width', '-w', type=int, help="Width to resize the image")
def main(infile, outfile, height, width):
    """cli function for findscore
    """
    try:
        if height is None and width is None:
            score(infile, outfile, height=cfg.HEIGHT, width=cfg.WIDTH)
        else:
            score(infile, outfile, height, width)
    except Exception as err:
        helper()
        print('Error:' , err)

if __name__ == '__main__':
    main()

