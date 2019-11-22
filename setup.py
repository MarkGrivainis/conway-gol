from setuptools import setup

setup(
    name="Conway GOL",
    version="0.0.0",
    author="M. Grivainis",
    packages=["src"],
    # scripts=['bin/stowe-towels.py','bin/wash-towels.py'],
    description="Simple implementation of Conway's Game of life",
    # long_description=open('README.txt').read(),
    install_requires=[
        "numba == 0.46.0",
        "numpy == 1.17.4",
        "matplotlib == 3.1.2",
    ],
)
