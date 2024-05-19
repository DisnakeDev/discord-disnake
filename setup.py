import re
from setuptools import setup


requirements = []
with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.readlines()

version = ""
with open("discord/__init__.py", encoding="utf-8") as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)  # type: ignore

if not version:
    raise RuntimeError("version is not set")

readme = ""
with open("README.md", encoding="utf-8") as f:
    readme = f.read()

packages = [
    "discord",
    "discord.types",
    "discord.ui",
    "discord.webhook",
    "discord.interactions",
    "discord.ext.commands",
    "discord.ext.tasks",
]

setup(
    name="discord-disnake",
    author="Rapptz, EQUENOS",
    url="https://github.com/DisnakeDev/discord-disnake",
    project_urls={
        "Documentation": "https://docs.disnake.dev/en/latest",
        "Issue tracker": "https://github.com/DisnakeDev/discord-disnake/issues",
    },
    version=version,
    packages=packages,
    license="MIT",
    description="A shim for disnake (Python wrapper for the Discord API)",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.8.0",
    classifiers=[
        "Development Status :: 7 - Inactive",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
