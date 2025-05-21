from setuptools import setup

setup(
    name="filesearch",
    author="Michael Koller",
    author_email="koller_michael@outlook.de",
    version="1",
    url="https://github.com/michael-koller-91/filesearch",
    packages=["filesearch"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "filesearch=filesearch.main:main",
        ],
    },
)
