#!/usr/bin/env python3

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
@click.option('--git/--no-git', envvar='JOT_NO_GIT_PUSH', default=True,
              help='Enable/Disable automatic git integration. default=enabled')
@click.option('--git-push/--no-git-push', envvar='JOT_NO_GIT_PUSH',
              default=True,
              help='Enable/Disable automatic git push.  default=enabled')
def jot(editor, directory, extension, category, name, git, git_push):
    if not name:
        name = datetime.date.today().isoformat()

    jot_dir = os.path.expanduser(directory)
    jot_cat_dir = os.path.join(jot_dir, category)

    if not os.path.exists(jot_cat_dir):
        os.makedirs(jot_cat_dir, exist_ok=True)

    jot_file = os.path.join(jot_cat_dir, name)
    jot_file += extension

    subprocess.call([editor, jot_file])

    git_dir = os.path.join(jot_dir, '.git')
    if git and os.path.exists(git_dir) and os.path.exists(jot_file):
        subprocess.call(['git', 'add', jot_file], cwd=jot_dir)
        commit_retcode = subprocess.call(
            ['git', 'commit', '-m', 'auto-commit by jot'], cwd=jot_dir)

        if commit_retcode == 0 and git_push:
            subprocess.call(['git', 'push'], cwd=jot_dir)


if __name__ == '__main__':
    jot()
