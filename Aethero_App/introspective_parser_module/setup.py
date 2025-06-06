from setuptools import setup, find_packages

setup(
    name="introspective_parser_module",
    version="0.1.0",
    description="Aethero Introspective Parser Module",
    author="Aethero Project",
    packages=find_packages(),
    install_requires=[
        "pydantic>=2.11.0",
        "tabulate>=0.9.0",
        "typing-extensions>=4.12.0"
    ],
    python_requires=">=3.8",
)
