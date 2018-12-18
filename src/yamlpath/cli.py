import click

def append_path(data, keys,path):
    if type(data) != dict:
	return
    for key in data:
	keys.append('.'.join(path + [key]))
	append_path(data[key], keys, path + [key])

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
