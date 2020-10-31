from setuptools import setup

setup(
    name='space_invaders',
    entry_points={
        'console_scripts': [
            'space_invaders = space_invaders.main:main'
        ]
    }
)
