import click
from skill_storage import FileStorage

skill_storage = FileStorage('temp')

@click.command()
@click.option('--name', prompt='Your name',
              help='The person adding skills.')
def hello(name):
    """Simple program that greets NAME for a total of COUNT times."""
    click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()
