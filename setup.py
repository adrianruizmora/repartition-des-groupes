import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="repartition_groupes_ruiz", # Replace with your own username
    version="0.0.1",
    author="Adrian Ruiz",
    py_modules=["repartition_groupes"],
    author_email="adrianruizmora@hotmail.com",
    description="Repartition des personnes dans groupes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adrianruizmora/repartition-des-groupes.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)