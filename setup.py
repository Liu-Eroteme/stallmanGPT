from setuptools import setup, find_packages

setup(
    name="stallmanGPT",
    version="1.0.0",
    author="Liu Eroteme",
    author_email="Liu@hellmann.cc",
    description="A Linux command generator and assistant using OpenAI GPT-3.5-turbo",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Liu-Eroteme/stallmanGPT",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    install_requires=[
        "openai",
    ],
    python_requires='>=3.6',
)
