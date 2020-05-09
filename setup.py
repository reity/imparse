from setuptools import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="imparse",
    version="0.0.0.1",
    packages=["imparse",],
    install_requires=[],
    license="MIT",
    url="https://github.com/reity/imparse",
    author="Andrei Lapets",
    author_email="a@lapets.io",
    description="Lightweight infinite-lookahead parser generator that "+\
                "supports basic grammars defined in a JSON format.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    test_suite="nose.collector",
    tests_require=["nose"],
)
