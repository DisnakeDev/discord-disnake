import re

from setuptools import setup

requirements = []


VERSION = "2.3.0"

requirements.append("disnake" + "==" + VERSION)

readme = ""
with open("README.md", encoding="utf-8") as f:
    readme = f.read()

packages = [
    "discord",
    "discord.ext.commands",
    "discord.ext.tasks",
    "discord.interactions",
    "discord.types",
    "discord.ui",
    "discord.webhook",
]

setup(
    name="discord-disnake",
    author="Rapptz, EQUENOS",
    url="https://github.com/DisnakeDev/discord-disnake",
    project_urls={
        "Homepage:": "https://disnake.dev/",
        "Documentation": "https://docs.disnake.dev/en/latest",
        "Issue tracker": "https://github.com/DisnakeDev/discord-disnake/issues",
    },
    version=VERSION,
    packages=packages,
    license="MIT",
    description="A shim for disnake (Python wrapper for the Discord API)",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.8.0",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
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
