from setuptools import setup, find_packages

setup(
    name='dramacool',
    version='0.1',
    packages=find_packages(),
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
