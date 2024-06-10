from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='dramacool',
    version='0.5',
    author="Abhi Nandan",
    author_email="nandan645@protonmail.com",
    description="A simple cli package that lets you download asian webseries/dramas/movies from dramacool website.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nandan645/dramacool-dl",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'dramacool=dramacool.main:drama',
        ],
    },
    install_requires=[
        # List your package dependencies here
        'requests',
        'beautifulsoup4',
        'yt-dlp',
        'aria2',
    ],

)
