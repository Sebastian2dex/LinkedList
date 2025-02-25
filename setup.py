from setuptools import setup, find_packages

setup(
    name="linked_list",  
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],  
    author="Sebastian",
    author_email="uselessjey@gmail.com",
    description="A simple linked list implementation in Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Sebastian2dex/LinkedList",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License", 
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

