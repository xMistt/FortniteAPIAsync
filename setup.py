import setuptools
import re

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('FortniteAPIAsync/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

setuptools.setup(
    name="FortniteAPIAsync",
    version=version,
    author="xMistt",
    description="Asynchronous Python wrapper for Fortnite-API.com.",
    project_urls={
        "Documentation": "https://github.com/xMistt/FortniteAPIAsync/wiki",
        "Issues": "https://github.com/xMistt/FortniteAPIAsync/issues",
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xMistt/FortniteAPIAsync",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'aiohttp',
    ],
)