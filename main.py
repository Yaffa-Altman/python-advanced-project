import click

from graghs import get_histogram_gragh_about_function_lengths, get_number_of_issues_per_file, \
    get_pie_chart_gragh_about_number_of_issues, all_graghs
from wit import Wit
from test import *


@click.group()
def cli():
    pass


@click.command()
def init_cmd():
    wit.init()


@click.command()
@click.argument('file_name')
def add_cmd(file_name):
    wit.add(file_name)


@click.command()
def log_cmd():
    wit.log()


@click.command()
def status_cmd():
    wit.status()


@click.command()
@click.argument('commit_id')
def checkout_cmd(commit_id):
    wit.checkout(commit_id)


@click.command()
@click.argument('message')
def commit_cmd(message):
    wit.commit(message)


cli.add_command(init_cmd, name='init')
cli.add_command(add_cmd, name='add')
cli.add_command(log_cmd, name='log')
cli.add_command(status_cmd, name='status')
cli.add_command(checkout_cmd, name='checkout')
cli.add_command(commit_cmd, name='commit')

if __name__ == '__main__':
    path = r'C:\Users\The user\Desktop\תכנות\שנה ב\Python\Python מתקדם\HomeWork\3'

    open_dir(path)
    all_graghs()
    wit = Wit()
    cli()
    # print(wit.ast())

