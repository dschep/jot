Jot
===

Jot is a CLI utility that lets you write notes with out having to worry about
where they're stored. By default, all notes are stored in a git repo at
``~/.jot`` in markdown and automatically pushed to a git repo.


Install
-------
::
    sudo pip install jot-notes

Usage
-----
::
    $ # Edit today's note, ie: ~/.jot/YYYY-MM-DD.md
    $ jot
    $ # edit a note in a category with a specific name, ie: ~/.jot/foo/bar.md
    $ jot -c foo -n bar
    $ # disable git integration


Configuring Jot
---------------
Most of Jot's configuration can be done on the CLI & with environment
variables. Here are the relevant environment variables:

 * EDITOR - what text editor to use, defaults to ``nano``
 * JOT_DIR - where to store jot's notes, defaults to ``~/.jot``
 * JOT_NO_GIT - disable jot's git integration
 * JOT_NO_GIT_PUSH - disable automatic ``git push``



