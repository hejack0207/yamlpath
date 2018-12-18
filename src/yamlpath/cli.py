import click

@click.command()
@click.option('--name', prompt='Your name', help='The person to greet.')
def cli(file):
    """show all keys recursively for specified yaml file"""
    for x in range(count):
        click.echo('%s' % name)

if __name__ == '__main__':
    cli()
