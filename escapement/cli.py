"""Console script for escapement."""
import sys
import click

from .escapement import escapement


@click.command()
def main(args=None):
    """Console script for escapement."""
    click.echo("Escapement: Understand your projects")
    escapement()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
