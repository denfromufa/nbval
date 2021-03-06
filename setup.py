from setuptools import setup

setup(
    name="nbval",
    version="0.3",
    author="Laslett, Cortes, Kluyver, Fangohr",
    packages = ['nbval'],

    # the following makes a plugin available to pytest
    entry_points = {
        'pytest11': [
            'nbval = nbval.plugin',
        ]
    },
)
