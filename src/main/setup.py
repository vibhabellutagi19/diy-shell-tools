"""Setup file for dyi-shell-tools package."""

from setuptools import setup


def read_version():
    """Read the version from the VERSION file."""
    with open("../../../VERSION", "r", encoding="utf-8") as version_file:
        return version_file.read().strip().replace("-", ".")


setup(
    author="vibhavari bellutagi",
    author_email="vibhavari.bellutagi@gmail.com",
    description="""A dyi shell tools, mimics the shell commands like wc, grep, ls etc""",
    name="dyi-shell-tools",
    version=read_version(),
)
