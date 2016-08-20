from setuptools import setup, find_packages
from sys import version_info


setup(
    name='jot-notes',

    version='0.1.0',

    description='A simple utility for writing notes without remembering where you put them.',

    url='https://github.com/dschep/jot',

    author='Daniel Schep',
    author_email='dschep@gmail.com',

    license='GPLv3',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Environment :: Console',

        'Intended Audience :: End Users/Desktop',

        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='notes git markdown',

    py_modules=['jot'],

    install_requires=['click'],

    entry_points={
        'console_scripts': [
            'jot = jot:jot',
        ],
    },
)
