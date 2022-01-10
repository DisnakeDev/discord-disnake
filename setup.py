import re

from setuptools import setup

requirements = []
versions = []
with open("version.txt", "r") as f:
    for line in f:
        if line.startswith("#"):
            continue
        if not (ver := line.strip()):
            continue
        versions.append(ver)
        if len(versions) == 2:
            break
    read_version, sub_version = versions


requirements.append("disnake" + "==" + read_version)


version = ""
with open("discord/__init__.py", encoding="utf-8") as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)  # type: ignore

if not version:
    raise RuntimeError("version is not set")

if read_version != version:
    raise RuntimeError(f"version.txt is {read_version}, but __init__.py is {version}")

version += "." + sub_version
if version.strip(".").count(".") != 3:
    raise RuntimeError(
        'Fourth digit of version must be configured properly. Current configured version is "{}"'.format(
            version
        )
    )


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
