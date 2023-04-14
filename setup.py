from setuptools import setup, find_packages

setup(
    name="stallmangpt",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["openai"],
    entry_points={"console_scripts": ["stallmangpt = stallmangpt:main"]},
)
