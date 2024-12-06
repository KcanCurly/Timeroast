from setuptools import setup, find_packages

setup(
    name="Timeroast",
    version="0.0.1",
    author="KcanCurly",
    description="A script to dump files and folders remotely from a Windows SMB share.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KcanCurly/Timeroast",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "timeroast.py=src.timeroast:main",  
        ],
    },
)