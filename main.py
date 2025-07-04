#!/usr/bin/env python3
import click

from plugins.etl import ETL


@click.command()
@click.option("--config", "-c", required=True, help="Path to YAML configuration file")
def main(config):
    """Run ETL pipeline from configuration file."""
    etl = ETL.from_yaml(config)
    etl.run()


if __name__ == "__main__":
    main()
