from distutils.core import setup

setup(
    name="mtaa",
    version="0.1.0",
    description="A package consisting of all Tanzania locations from region to streets in a easy accessible way",
    url="https://github.com/Kalebu/nida",
    download_url="https://github.com/Kalebu/nida/archive/0.1.tar.gz",
    author="Jordan Kalebu",
    author_email="isaackeinstein@gmail.com",
    license="MIT",
    packages=["mtaa"],
    keywords=[
        "nida",
        "nida api"
        "nida python package"
        "python nida"
        "tanzania nida",
        "python-tanzania",
    ],
    include_package_data=True,
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
