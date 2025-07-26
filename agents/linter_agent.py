import subprocess


def run_linters(path="."):
    subprocess.run(["black", path])
    subprocess.run(["flake8", path])
