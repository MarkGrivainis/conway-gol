from setuptools import setup

setup(
    name="Conway GOL",
    version="0.0.0",
    author="M. Grivainis",
    packages=["conway"],
    package_dir={"conway": "src/conway"},
    # scripts=['bin/stowe-towels.py','bin/wash-towels.py'],
    description="Simple implementation of Conway's Game of life",
    # long_description=open('README.txt').read(),
    install_requires=[
        "numba == 0.46.0",
        "numpy == 1.22.0",
        "matplotlib == 3.1.2",
    ],
)
