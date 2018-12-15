#!/usr/bin/env python
import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def cli(count, name):
    """yamlpath 'path to yaml file'"""
    for x in range(count):
        click.echo('%s' % name)

if __name__ == '__main__':
    cli()
