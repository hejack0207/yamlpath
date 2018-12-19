import click
import yaml

def append_path(data, keys,path):
    if type(data) != dict or type(data) != list:
	return

    if type(data) == dict:
        for key in data:
            keys.append('.'.join(path + [key]))
            append_path(data[key], keys, path + [key])

    if type(data) == list:
        for n in range(len(data)):
            keys.append('.'.join(path + [n]))
            append_path(data[n], keys, path + [key])


@click.command()
@click.argument('yamlfile', type=click.Path())
def cli(yamlfile):
    """show all keys recursively for specified yaml file"""
    keys=[]
    try:
        data = yaml.load(open(yamlfile))
        append_path(data,keys, [])
    except yaml.YAMLError:
        click.echo(f"Warn: ParseError in {yamlfile}", err=True)

    click.echo(keys)

if __name__ == '__main__':
    cli()

# vim: sts=-1 sw=4
