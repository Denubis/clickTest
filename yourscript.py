import click



@click.group()
def cli():
	pass


@click.command()
def hello():
    """Example script."""
    click.echo('Hello World!')

@click.command()
def hi():
    """Example script."""
    click.echo('Hi World!')    

cli.add_command(hello)    
cli.add_command(hi)    