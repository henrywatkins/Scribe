from setuptools import setup

setup(
    name="scribe",
    version="0.0",
    py_modules=["scribe"],
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "scribe = scribe.scribe:cli",
        ],
    },
)
