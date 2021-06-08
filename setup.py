from setuptools import setup

setup(
    name="Visual Plotter",
    version="0.0.1",
    packages=["visualplotter"],
    entry_points={
        "console_scripts": [
            "VSPlotter = visualplotter.__main__:main"
        ]
    }
)