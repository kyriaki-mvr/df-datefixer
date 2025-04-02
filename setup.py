from setuptools import setup, find_packages

setup(
    name="df-datefixer",
    version="0.1.0",
    description="Simple package to automatically standardize dates in Pandas DataFrames.",
    author="Kyriaki Mavrooulou",
    author_email="kyriaki@quanterra.gr",
    packages=find_packages(where="src"),
    package_dir={'': 'src'},
    install_requires=[
        'pandas',
        'python-dateutil',
    ],
    python_requires=">=3.7",
)
