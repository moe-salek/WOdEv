import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="WOdEv",
    version="1.0.1",
    description="Week Odd (or) Even",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/MohammadSalek/WOdEv",
    author="Mohammad Salek",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["jdatetime>=3.6.2"],
    dependency_links=[
        'https://pypi.org/project/jdatetime/'
    ],
    entry_points={
        "console_scripts": [
            "wodev=wodev.__main__:main",
        ]
    },
)
