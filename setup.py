from os.path import dirname, join
from setuptools import setup, find_packages

name = "ipynotebookwidget"
brand = "ripxl"
full_name = "Dead Pixel Collective"

with open(join(dirname(__file__), name, "__init__.py")) as fp:
    for i, line in enumerate(fp.readlines()):
        if line.startswith("__version__ ="):
            __version__ = line.split(" ")[2][1:-2]

setup(
    name=name,
    version=__version__,
    url=f"https://github.com/{brand}/{name}",
    author=full_name,
    author_email=f"{brand}@groups.google.com",
    description="Use Notebooks and Kernels like Widgets",
    packages=find_packages(),
    install_requires=[
        "ipywidgets >=7.0.0",
        "jupyter_client >=5.2.1",
        "nbformat >=4.4.0",
    ],
    license="BSD-3-Clause",
    include_package_data=True,
    zip_safe=False,
)