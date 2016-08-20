#!/usr/bin/env python

"""
Usage: jot [OPTIONS]

Options:
  -e, --editor TEXT           Editor to use, defaults to the $EDITOR envvar
  -d, --directory TEXT        Directory to store jots, also reads $JOT_DIR.
                              default=~/.jot
  -E, --extension TEXT        File extension for jots, also reads $JOT_EXT.
                              default=.md
  -c, --category TEXT         A category(subdir) to put the jot in
  -n, --name TEXT             Name of the jot. Defaults to todays ISO8601 date
  --git / --no-git            Enable/Disable automatic git integration.
                              default=enabled
  --git-push / --no-git-push  Enable/Disable automatic git push.
                              default=enabled
  --template TEXT             Default jot contents as a python format string.
                              default="# {name}

                              "
  --help                      Show this message and exit.
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
@click.option('--git/--no-git', envvar='JOT_NO_GIT', default=True,
              help='Enable/Disable automatic git integration. default=enabled')
@click.option('--git-push/--no-git-push', envvar='JOT_NO_GIT_PUSH',
              default=True,
              help='Enable/Disable automatic git push.  default=enabled')
@click.option('--template', envvar='JOT_TEMPLATE',
              default='# {name}\n\n',
              help=('Default jot contents as a python format string.  '
                    'default="# {name}\n\n"'))
def jot(editor, directory, extension, category, name, git, git_push, template):
    if not name:
        name = datetime.date.today().isoformat()

    jot_dir = os.path.expanduser(directory)
    cat_dir = os.path.join(jot_dir, category)
    git_dir = os.path.join(jot_dir, '.git')

    if not os.path.exists(jot_dir):
        os.mkdir(jot_dir)

    if not os.path.exists(cat_dir):
        os.mkdir(cat_dir)

    if git and not os.path.exists(git_dir):
        repo = click.prompt('Enter a git remote')
        subprocess.call(['git', 'init'], cwd=jot_dir)
        subprocess.call(['git', 'remote', 'add', 'origin', repo], cwd=jot_dir)
        subprocess.call(['git', 'branch', '--set-upstream'], cwd=jot_dir)

    jot_file = os.path.join(cat_dir, name) + extension

    if not os.path.exists(jot_file) and template:
      open(jot_file, 'w').write(template.format(name=name))

    subprocess.call([editor, jot_file])

    if git and os.path.exists(jot_file):
        subprocess.call(['git', 'add', jot_file], cwd=jot_dir)
        commit_retcode = subprocess.call(
            ['git', 'commit', '-m', 'auto-commit by jot'], cwd=jot_dir)

        if commit_retcode == 0 and git_push:
            subprocess.call(['git', 'push'], cwd=jot_dir)


if __name__ == '__main__':
    jot()
