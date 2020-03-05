import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fingerprint-oneplace-jbinggi",
    version="0.0.7",
    author="JBinggi",
    author_email="juerg.binggeli@gmail.com",
    description="Raspberry Pi Fingerprint Library to connect with Oneplace",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jbinggi/Oneplace_Fingerprint",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts=['bin/oneplace-fingerprint'],
    python_requires='>=3.5',
)