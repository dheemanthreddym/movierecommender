from setuptools import setup


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


AUTHOR_NAME = "Dheemanth Reddy"
SRC_REPO = "src"
LIST_OF_PACKAGES = ["streamlit"]

setup(
    name="SRC_REPO",
    version="0.1.0",
    author=AUTHOR_NAME,
    author_email="dheemanthreddym@gmail.com",
    description="a small package for movie recommendation system using streamlit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    package=[SRC_REPO],
    python_requires=">=3.7",
    install_requires=LIST_OF_PACKAGES,
    

)
