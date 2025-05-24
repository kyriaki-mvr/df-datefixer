from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="df-datefixer",
    version="1.0.2",
    description="A package to automatically standardize dates in Pandas DataFrames.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kyriaki-mvr/df-datefixer",
    author="Kyriaki Mavrooulou",
    author_email="kyriaki@quanterra.gr",
    packages=find_packages(),
    package_dir={'': 'src'},
    install_requires=[
        'pandas',
        'python-dateutil',
    ],
    python_requires=">=3.7",
    license="MIT"
)
