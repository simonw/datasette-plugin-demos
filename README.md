# datasette-plugin-demos

Examples of plugins for Datasette.

The plugins feature is currently extremely unstable and under active development -
see https://github.com/simonw/datasette/issues/14

This repository will host example plugins as the feature develops. It also means
I can ship a package to PyPI to ensure plugin registration works as intended.

## How to release

First, bump the VERSION in `setup.py`

    python3 setup.py sdist
    twine upload dist/*
