#!/bin/python3

import os
import shutil

import click
import PyInstaller.__main__


def delete_path(path):
    if (os.path.exists(path)):
        print(f"found {path}, delete...")
        if (os.path.isdir(path)):
            shutil.rmtree(path)
        else:
            os.remove(path)


def path(*args):
    return os.path.join(*args)


PROJECT_NAME = "MerlinStructs"
UPX_DIR = path("tools", "upx-4.0.2-amd64_linux")


@click.group()
def cli():
    pass


@cli.command()
def build():
    print("build...")
    PyInstaller.__main__.run([
        path('src', 'main.py'),
        f'--upx-dir={UPX_DIR}',
        '--onefile',
        f'-n={PROJECT_NAME}'
    ])


@cli.command()
def clean():
    print("clean...")
    delete_path("./build")
    delete_path("./dist")
    delete_path(f"./{PROJECT_NAME}.spec")


if __name__ == "__main__":
    cli()
