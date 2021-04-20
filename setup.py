from setuptools import setup

setup(
    name="nida",
    version="0.1.2",
    description="A python libary to Easy fetching user information based on National ID (Tanzania)",
    url="https://github.com/Kalebu/nida",
    download_url="https://github.com/Kalebu/Nida/archive/0.2.tar.gz",
    author="Jordan Kalebu",
    author_email="isaackeinstein@gmail.com",
    license="MIT",
    packages=["nida"],
    keywords=[
        "nida",
        "nida api"
        "nida python package"
        "python nida"
        "tanzania nida",
        "python-tanzania",
    ],
    install_requires=[
        'addict',
        'requests',
        'pillow'
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
