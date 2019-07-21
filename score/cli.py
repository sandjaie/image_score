import click
from findscore import main as score


@click.command()
@click.option('--infile', '-i', help="Enter the input file path")
@click.option('--outfile', '-o', help="Enter the output file path")
@click.option('--height', '-h', type=int)
@click.option('--width', '-w', type=int)
def main(infile, outfile, height, width):
    try:
        score(infile, outfile, height, width)
    except Exception as err:
        print(err)

if __name__ == '__main__':
    main()

