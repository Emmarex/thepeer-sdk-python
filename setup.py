from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='thepeer-sdk',
    version='0.0.1',
    author="Tairu Oluwafemi Emmanuel",
    author_email="developer.emmarex@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Emmarex/thepeer-sdk-python",
    download_url="",
    keywords=['thepeer'],
    include_package_data=True,
    packages=find_packages(),
    python_requires='~=3.7',
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.10"
        "Programming Language :: Python :: 3.11"
        "License :: OSI Approved :: Apache Software License",
        "Development Status :: 4 - Beta",
        # "Development Status :: 6 - Mature",
        "Intended Audience :: Developers"
    ],
)
