from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "colorama==0.4.6",
        "numpy==2.0.1",
        "pandas==2.2.2",
        "python-dateutil==2.9.0.post0",
        "pytz==2024.1",
        "six==1.16.0",
        "tzdata==2024.1",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple example Python package",
    url="https://github.com/yourusername/my_module",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
