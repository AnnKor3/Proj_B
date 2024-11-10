
from typing import List
from setuptools import find_packages, setup


def get_requirements() -> List[str]:
    req_lst: List[str] = []
    try:
          with open('requirements.txt', 'r') as file:
                lines = file.readlines()
                for line in lines:
                    req = line.strip()
                    if req and req != '-e .':
                        req_lst.append(req)
    except FileNotFoundError:
        print('requirements.txt file not found')

    return req_lst

setup(
    name="Proj_B",
    version="0.0.1",
    author="Anna MK",
    packages=find_packages(),
    install_requires=get_requirements()
)