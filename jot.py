#!/usr/bin/env python

"""
A simple utility for writing notes without remembering where you put them.

Usage: jot [OPTIONS]

Options:
  -e, --editor TEXT     Editor to use, defaults to the $EDITOR envvar
  -d, --directory TEXT  Directory to store jots, also reads $JOT_DIR.
                        default=~/.jot
  -E, --extension TEXT  File extension for jots, also reads $JOT_EXT.
                        default=.md
  -c, --category TEXT   A category(subdir) to put the jot in
  -n, --name TEXT       Name of the jot. Defaults to todays ISO8601 date
  --help                Show this message and exit.
"""

import datetime
import os
import subprocess

import click


@click.command()
@click.option('--editor', '-e', envvar='EDITOR', default='nano',
              help='Editor to use, defaults to the $EDITOR envvar')
@click.option('--directory', '-d', envvar='JOT_DIR', default='~/.jot',
              help=('Directory to store jots, also reads $JOT_DIR.'
                    ' default=~/.jot'))
@click.option('--extension', '-E', envvar='JOT_EXT', default='.md',
              help=('File extension for jots, also reads $JOT_EXT.'
                    ' default=.md'))
@click.option('--category', '-c', default='',
              help='A category(subdir) to put the jot in')
@click.option('--name', '-n',
              help='Name of the jot. Defaults to todays ISO8601 date')
def jot(editor, directory, extension, category, name):
    if not name:
        name = datetime.date.today().isoformat()

    jot_file = os.path.join(os.path.expanduser(directory), category, name)
    jot_file += extension

    subprocess.call([editor, jot_file])

if __name__ == '__main__':
    jot()
